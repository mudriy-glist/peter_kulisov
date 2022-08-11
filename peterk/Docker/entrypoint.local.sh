# Author: Peter Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 11/08/2022
#!/bin/bash

python3 manage.py makemigrations &
python3 manage.py migrate &
python3 manage.py collectstatic --no-input --clear &

gunicorn peterk.wsgi -w 1 -b 0.0.0.0:8000 --timeout 120 --workers 5 --worker-class gevent
