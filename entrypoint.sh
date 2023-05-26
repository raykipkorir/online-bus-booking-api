#! /usr/bin/env bash
set -e
set -x

python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input

gunicorn core.wsgi
