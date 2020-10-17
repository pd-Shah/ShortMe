from flask import (
    Blueprint,
    render_template,
)

bp = Blueprint(
    "error",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/error"
)


@bp.app_errorhandler(404)
def error_404(e, ):
    msg = "Things Break Sometimes."
    code = 404
    return render_template("error/404.html", msg=msg, code=code), code


@bp.app_errorhandler(413)
def error_413(e, ):
    msg = "File is Too Large!"
    code = 413
    return render_template("error/413.html", msg=msg, code=code), code
