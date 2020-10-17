from json import dumps
from flask import Blueprint, jsonify, request
from app.init import redis
from . import logics as lg
from flask_login import login_user, current_user
from app.packages.short import logics as sh_lg

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/login", methods=["GET", "POST"])
@lg.error_check
def login():
    if request.method == "POST" and request.is_json:
        user = request.get_json()
        if user is not None:
            user = lg.check_to_login(user)
            if user:
                login_user(user=user, remember=False, )
                token = current_user.generate_signature().strip().decode()
                urls = sh_lg.get_user_urls(current_user)
                [redis.set(url.name, url.url) for url in urls]
                return jsonify(status=200, message={"msg": "token generated.", "token": token}), 200
    return jsonify(status=200, message="wrong request.", ), 200


@bp.route("/signup", methods=["GET", "POST"])
@lg.error_check
def signup():
    if request.method == "POST" and request.is_json:
        user = request.get_json()
        if user is not None:
            user = lg.check_to_sign_up(user)
            if user:
                return jsonify(status=200, message={"msg": "signup.", }), 200
    return jsonify(status=200, message="wrong request.", ), 200


@bp.route("/get-urls", methods=["GET", "POST"])
@lg.token_required
@lg.error_check
def get_user_urls():
    urls = sh_lg.get_user_urls(current_user)
    urls = lg.dump_urls(urls)
    return jsonify(status=200, message={"msg": "user urls.", "urls": urls}), 200


@bp.route("/add-url", methods=["GET", "POST"])
@lg.token_required
@lg.error_check
def add_url():
    if request.is_json:
        url = request.json.get("url")
        if url is not None:
            url = lg.add_url(url)
            redis.set(url.name, url.url)
            return jsonify(status=200, message={"msg": "url added", "url": redis.get(url.name).decode("utf-8")}), 200
    return jsonify(status=200, message="wrong request.", ), 200


@bp.route("/get-url", methods=["GET", "POST"])
@lg.token_required
@lg.error_check
def get_user_url():
    if request.is_json:
        name = request.json.get("name")
        if name is not None:
            url = redis.get(name).decode("utf-8")
            return jsonify(status=200, message={"msg": "url", "url": url}), 200
    return jsonify(status=200, message="wrong request.", ), 200