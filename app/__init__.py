from os import makedirs
from flask import (
    Flask,
    render_template,
)
from settings import config
from .init import (
    db,
    migrate,
    login,
    redis,
)
from app.packages import authentication
from app.packages import error
from app.packages import admin
from app.packages import api


def create_app():
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
    )
    app.config.from_object(config)
    makedirs(
        name=app.instance_path,
        exist_ok=True,
    )
    app.config.from_pyfile(filename="settings.py", silent=False)
    db.init_app(app=app)
    migrate.init_app(app, db, )
    redis.init_app(app, )
    login.init_app(app, )
    login.anonymous_user = authentication.models.AnonymousUser
    app.register_blueprint(authentication.bp)
    app.register_blueprint(error.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(api.bp)

    @app.route("/", methods=["GET", ])
    def index():
        return render_template("base.html")

    @app.shell_context_processor
    def load_data():
        a = authentication.models.User.query.get(1)
        m = authentication.models.User.query.get(2)
        u = authentication.models.User.query.get(3)
        return dict(
            app=app,
            User=authentication.models.User,
            Image=authentication.models.Image,
            Role=authentication.models.Role,
            u=u,
            db=db,
            m=m,
            a=a,
        )

    return app
