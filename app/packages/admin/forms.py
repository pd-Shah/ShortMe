from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    PasswordField,
    FileField,
    DateTimeField,
    SelectField,
    SubmitField,
)
from wtforms.validators import (
    Email,
    Length,
)
from wtforms.widgets import (
    TextArea,
)


class UserAdminForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)

    email = StringField(
        label="email",
        validators=[Email(), Length(1, 64)],
    )
    password = PasswordField(
        label="password",
        validators=[Length(0, 64), ],
    )
    name = StringField(label="name", validators=[Length(0, 64), ])
    family = StringField(label="family", validators=[Length(0, 64), ])
    username = StringField(label="username", validators=[Length(0, 64), ])
    photo = FileField(label="profile picture")
    role = SelectField(label="role", validate_choice=False)
    location = StringField(label="location")
    about_me = StringField(label="describe your self", widget=TextArea(), validators=[Length(0, 256), ])
    last_seen = DateTimeField(label="last seen")
    submit = SubmitField(
        label="Update",
    )
