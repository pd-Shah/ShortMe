from functools import wraps
from flask import abort, jsonify, request
from flask_login import current_user
from app.packages.authentication.models import User
from .schemas import LoginUser, UserUrl
from app.init import db
from app.packages.short.models import ShortUrl


def error_check(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except Exception as e:
            error_message = e.args
            return jsonify(status=500, message={"error_message": error_message, }), 500
        return result

    return decorated_function


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.method == "POST":
            token = request.headers.get('authorization', None)
            if token is not None:
                if not current_user.validate_signature(token):
                    return jsonify(status=500, message={"error_message": "token is not valid.", }), 500
                return f(*args, **kwargs)
            return jsonify(status=500, message={"error_message": "authorization format is not valid.", }), 500
        return jsonify(status=200, message="wrong request.", ), 200
    return wrapper


def check_to_login(user, ):
    login_user = LoginUser()
    login_user.load(user)
    email = user['email']
    password = user['password']
    user = User.query.filter_by(email=email).first()
    if user is None:
        return False
    if not user.verify_password(password):
        return False
    user.update_last_seen()
    return user


def check_to_sign_up(user_obj, ):
    login_user = LoginUser()
    login_user.load(user_obj)
    email = user_obj["email"]
    user = User(email=email)
    user.password = user_obj["password"]
    user.is_active = True
    db.session.add(user)
    db.session.commit()
    return user


def dump_urls(urls, ):
    url = UserUrl()
    urls = url.dump(urls, many=True)
    return urls


def add_url(url, ):
    url = ShortUrl(url=url, user=current_user, )
    url.name = ShortUrl.create_short_url(url.url)
    exist = ShortUrl.query.filter_by(url=url.url).first()
    if exist is None:
        db.session.add(url)
        db.session.commit()
    return url


