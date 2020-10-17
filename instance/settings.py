from os import environ
from os.path import (
    abspath,
    dirname,
    join
)

# SQLALCHEMY_DATABASE_URI = environ.get(
#     key="DATABASE_URI",
#     default="sqlite:///{0}".format(join(abspath(dirname(__file__)), "bd.db"))
# )
SQLALCHEMY_TRACK_MODIFICATIONS = False
