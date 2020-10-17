#!/bin/bash
source venv/bin/activate &&
rm -rf migrations/versions/* &&
python dropdb.py &&
rm -rf app/packages/authentication/static/images/*.png &&
rm -rf app/packages/authentication/static/images/*.jpg &&
rm -rf app/packages/authentication/static/images/*.gif &&
rm -rf app/packages/authentication/static/images/*.jpeg