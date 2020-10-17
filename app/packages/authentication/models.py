from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer
from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)
from flask import (
    current_app,
)
from flask_login import (
    UserMixin,
    AnonymousUserMixin,
)
from app.init import db


class Permission:
    FOLLOW = 0b00001
    COMMENT = 0b00010
    WRITE = 0b00100
    MODERATE = 0b01000
    ADMIN = 0b10000


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(length=64), unique=True, )
    users = db.relationship("User", back_populates="role", lazy="dynamic")
    permissions = db.Column(db.Integer, )

    def __init__(self, *args, **kwargs):
        super(Role, self).__init__(*args, **kwargs)
        if self.permissions is None:
            self.permissions = 0b00000

    def __repr__(self):
        return "<Role {0}>".format(self.name)

    def add_permission(self, permission):
        if not self.has_permission(permission):
            self.permissions += permission

    def has_permission(self, permission):
        return self.permissions & permission == permission

    def reset_permission(self, ):
        self.permissions = 0b00000

    def remove_permission(self, permission):
        if self.has_permission(permission):
            self.permissions -= permission


class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True, )
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="photo")


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(length=256, ), )
    family = db.Column(db.String(length=256, ), )
    username = db.Column(db.String(length=256, ), unique=True, )
    photo = db.relationship("Image", back_populates="user", uselist=False)
    short_urls = db.relationship("ShortUrl", back_populates="user", )
    password_hash = db.Column(db.String(length=256, ), )
    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
    )
    role = db.relationship("Role", back_populates="users", )
    email = db.Column(db.String(length=256), unique=True)
    location = db.Column(db.String(length=256))
    about_me = db.Column(db.Text())
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean(), default=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if self.role is None:
            if self.email == current_app.config["ADMIN"]:
                self.role = Role.query.filter_by(name="admin").first()
                self.is_active = True
            else:
                self.role = Role.query.filter_by(name="user").first()

    @property
    def password(self):
        raise AttributeError("[-] Setting password directly is not allowed!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {0}>".format(self.name)

    def can(self, permission):
        if permission is not None:
            return self.role.has_permission(permission)
        return False

    def update_last_seen(self, ):
        self.last_seen = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def get_photo_url(self, ):
        if self.photo:
            photo = self.photo
            return str(photo.id) + current_app.config.get("SAVE_EXTENSION")

    def generate_signature(self, exp=60000):
        serializer = TimedJSONWebSignatureSerializer(
            secret_key=current_app.config['SECRET_KEY'],
            salt='pd',
            expires_in=exp, )
        return serializer.dumps(
            {'code': self.id, }
        )

    def validate_signature(self, token):
        result = False
        serializer = TimedJSONWebSignatureSerializer(
            secret_key=current_app.config["SECRET_KEY"],
            salt='pd',
        )
        try:
            data = serializer.loads(token)
            if data.get('code') == self.id:
                result = True
        except Exception as e:
            print(e)
        return result


class AnonymousUser(AnonymousUserMixin, ):
    def can(self, ):
        return False

    def validate_signature(self, *args, **kwargs):
        return False
