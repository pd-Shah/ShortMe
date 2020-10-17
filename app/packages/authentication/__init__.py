from time import time
from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    request,
    url_for,
)
from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required,
    fresh_login_required,
)
from .forms import (
    LoginForm,
    SignUpForm,
    UpdateProfileForm,
)
from .logics import (
    check_to_login,
    get_user_by_username,
    check_to_sign_up,
    allowed_file,
    save_file,
    update_profile,
    check_activate_user_by_signature,
    # send_verification_email,
)
from app.packages.utils import is_url_safe

bp = Blueprint(
    name="authentication",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/auth",
    static_folder="static",
)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = check_to_login(form)
        if user:
            if user.is_active:
                nxt = request.args.get('next')
                login_user(
                    user=user,
                    remember=False,
                )
                flash("[+] welcome %s" % current_user.username)
                if is_url_safe(nxt):
                    return redirect(nxt)
                else:
                    return redirect("/")
            else:
                flash("[-] Your account is not activated.")
                flash(
                    "[+] An email verification has been sent to your email address.")
                flash("[-] Check your email for activation.")
                # send_verification_email(user_email=form.email.data)
                return redirect(request.url)
        else:
            flash("[-] Username & Password mixing is invalid.")
            return redirect(url_for('authentication.login'), )
    return render_template(
        "authentication/login.html",
        form=form,
    )


@bp.route("/logout", )
@login_required
def logout():
    logout_user()
    flash("[+] logout successfully done.")
    return redirect(url_for("index", ))


@bp.route("/<string:username>")
def user(username, ):
    user_obj = get_user_by_username(username=username)
    photo = 'default_profile.jpg'
    return render_template("authentication/profile.html", user=user_obj, file_name=photo)


@bp.route("/my-profile", methods=["GET", "POST"])
@fresh_login_required
def my_profile():
    form = UpdateProfileForm()
    photo = current_user.get_photo_url()
    if form.validate_on_submit():
        photo = request.files['photo']
        update_profile(form=form, photo=photo)
        return redirect(url_for('authentication.my_profile'))
    form.load_data()
    return render_template("authentication/my_profile.html", photo=photo, form=form, time=str(time()))


@bp.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        check_to_sign_up(form)
        flash("[+] Sing up successfully done.")
        return redirect(url_for('authentication.login'))
    return render_template("authentication/signup.html", form=form)


@bp.route('/verify/<token>', methods=["GET", "POST", ])
def verify_email(token, ):
    form = LoginForm()
    if form.validate_on_submit():
        user = check_to_login(form)
        if user:
            login_user(user=user, remember=False, force=True)
            check_activate_user_by_signature(token=token)
            return redirect("/")
        else:
            flash("[-] Username & Password mixing is invalid.")
            return redirect(request.url)
    return render_template(
        "authentication/login.html",
        form=form,
    )
    return redirect(url_for('authentication.login'))
