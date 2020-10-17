from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login = LoginManager()
login.login_view = "authentication.login"
login.refresh_view = "authentication.login"
db = SQLAlchemy()
migrate = Migrate()
redis = FlaskRedis()

