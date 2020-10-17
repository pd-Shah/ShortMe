from marshmallow import Schema, fields


class LoginUser(Schema):
    email = fields.Str(required=True, )
    password = fields.Str(required=True, )


class UserUrl(Schema):
    name = fields.Str(required=True, )
    url = fields.Str(required=True, )