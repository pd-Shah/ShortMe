from faker import Faker
from os import environ
from app.init import db
from app import create_app
from app.packages.authentication.models import User, Role, Permission, Image
from app.packages.short.models import  ShortUrl

app = create_app()
def get_admin_role():
    admin_permissions = [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.MODERATE,
                         Permission.ADMIN]
    admin_role = Role(name="admin", )
    [admin_role.add_permission(p) for p in admin_permissions]
    return admin_role


def get_moderator_role():
    moderator_permissions = [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.MODERATE]
    moderator_role = Role(name="moderator")
    [moderator_role.add_permission(p) for p in moderator_permissions]
    return moderator_role


def get_user_role():
    user_permissions = [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE]
    user_role = Role(name="user")
    [user_role.add_permission(p) for p in user_permissions]
    return user_role


with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
    db.session.commit()
    fake = Faker()
    app.config["ADMIN"] = environ.get("ADMIN")

    admin_role = get_admin_role()
    moderator_role = get_moderator_role()
    user_role = get_user_role()
    db.session.add_all([admin_role, moderator_role, user_role])
    db.session.commit()

    admin = User(name="pd", username="admin", email="pd.shahsafi@gmail.com", )
    admin.password = "1"
    db.session.add(admin)
    db.session.commit()

    url = ShortUrl(url=fake.url(), user=admin, )
    url.name = ShortUrl.create_short_url(url.url)
    db.session.add(url)

    url = ShortUrl(url=fake.url(), user=admin, )
    url.name = ShortUrl.create_short_url(url.url)
    db.session.add(url)

    url = ShortUrl(url=fake.url(), user=admin, )
    url.name = ShortUrl.create_short_url(url.url)
    db.session.add(url)
    db.session.commit()

    moderator = User(name="moderator", username="moderator", email="moderator@gmail.com", role=moderator_role)
    moderator.password = "1"
    db.session.add(moderator)
    db.session.commit()

    user = User(name=fake.name(), username=fake.name(), email=fake.email())
    user.password = "1"
    db.session.add(user)
    db.session.commit()

    user = User(name=fake.name(), username=fake.name(), email=fake.email())
    user.password = "1"
    db.session.add(user)
    db.session.commit()

    user = User(name=fake.name(), username=fake.name(), email=fake.email())
    user.password = "1"
    db.session.add(user)
    db.session.commit()
