#!/bin/bash

python3 manage.py makemigrations &
python3 manage.py migrate &
python3 manage.py collectstatic --no-input --clear &

gunicorn peterk.wsgi -w 1 -b 0.0.0.0:8000 --timeout 120 --workers 5 --worker-class gevent
