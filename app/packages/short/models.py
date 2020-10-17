from app.init import db
import uuid


class ShortUrl(db.Model):
    __tablename__ = "short_urls"
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(length=250), unique=True, )
    url = db.Column(db.String(length=250), )
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="short_urls")

    @staticmethod
    def create_short_url(url, ):
        return uuid.uuid4().hex

    @staticmethod
    def all_user_urls(user):
        return ShortUrl.query.filter_by(user=user).all()

    def __repr__(self):
        return "<Short {0}>".format(self.name)