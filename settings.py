from os import environ
from os.path import (
    abspath,
    dirname,
    join
)


class Config:
    from dotenv import load_dotenv
    load_dotenv()
    DEBUG = False
    TESTING = False
    SMTP_SERVER = environ.get("SMTP_SERVER")
    SMTP_USERNAME = environ.get("SMTP_USERNAME")
    SMTP_PASSWROD = environ.get("SMTP_PASSWROD")
    SMTP_USE_TLS = environ.get("SMTP_USE_TLS")
    SMTP_PORT = environ.get("SMTP_PORT")
    SERVER_NAME = environ.get("SERVER_NAME")
    SECRET_KEY = environ.get("SECRET_KEY")
    ADMIN = environ.get("ADMIN")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    SAVE_EXTENSION = ".jpg"
    BASE_DIR = abspath(dirname(__file__))
    MAX_CONTENT_LENGTH = int(environ.get("MAX_CONTENT_LENGTH_SIZE")) * int(
        environ.get("MAX_CONTENT_LENGTH_HEIGHT")) * int(environ.get("MAX_CONTENT_LENGTH_WEIGHT"))
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database:5432/postgres'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@0.0.0.0:5432/postgres'
    REDIS_URL = "redis://redis:6379/0"
    RQ_REDIS_URL = "redis://redis:6379/0"


class ProductionConfig(Config):
    UPLOAD_DIR = None


class DevelopmentConfig(Config):
    DEBUG = True
    UPLOAD_DIR = join(
        Config.BASE_DIR, 'app/packages/authentication/static/images')


class TestConfig(Config):
    TESTING = True
    UPLOAD_DIR = None


configs = {
    "development": "settings.DevelopmentConfig",
    "testing": "settings.TestConfig",
    "production": "settings.ProductionConfig",
}

config = configs[environ.get('FLASK_ENV', default="production")]
