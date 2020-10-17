from os.path import join
from os import remove
import requests
from functools import wraps
from flask_login import current_user
from flask import (
    abort,
    current_app,
    flash,
    url_for,
)
from app.init import (
    login,
    db,
)
from .models import (
    User,
    Image,
)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def check_to_login(user_obj, ):
    user = User.query.filter_by(email=user_obj.email.data).first()
    if user is None:
        return False
    if not user.verify_password(user_obj.password.data):
        return False
    user.update_last_seen()
    return user


def permission_required(permission, ):
    def decorator(f, ):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)

            return f(*args, **kwargs)

        return wrapper

    return decorator


def get_user_by_username(username):
    user = User.query.filter_by(username=username).first_or_404()
    return user


def check_to_sign_up(user_obj, ):
    password = user_obj.password.data
    email = user_obj.email.data
    user = User(email=email)
    user.password = password
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=email).first()
    token = user.generate_signature()
    # send_verification_email.queue(user_email=email, link=url_for("authentication.verify_email",
    #                                                              token=token, _external=True))
    flash("[+] An email verification has been sent to your email address.")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config.get("ALLOWED_EXTENSIONS")


def remove_old_photo():
    image = current_user.photo
    if image:
        remove(join(current_app.config['UPLOAD_DIR'], str(
            image.id) + current_app.config.get("SAVE_EXTENSION")))


def save_file(file):
    remove_old_photo()
    photo = Image()
    db.session.add(photo)
    current_user.photo = photo
    db.session.commit()
    filename = str(current_user.photo.id) + \
        current_app.config.get("SAVE_EXTENSION")
    file.save(join(current_app.config['UPLOAD_DIR'], filename))
    return filename


def update_profile(form, photo, ):
    # if user does not select file, browser also
    # submit an empty part without filename
    if photo and allowed_file(photo.filename):
        flash('[+] Upload successfully done.')
        save_file(photo)

    user = User.query.get(current_user.id)
    user.email = form.email.data
    user.name = form.name.data
    user.family = form.family.data
    user.username = form.username.data
    user.location = form.location.data
    user.about_me = form.about_me.data
    if form.password.data != "":
        user.password = form.password.data
    db.session.commit()
    flash("[+] Profile updated successfully.")
    return user


def check_activate_user_by_signature(token, ):
    if current_user.validate_signature(token):
        current_user.is_active = True
        db.session.commit()
