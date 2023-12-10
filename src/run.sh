#!/bin/bash

set -e

echo "Applying migrations"
python3 manage.py migrate --noinput

python3 manage.py initialize


if [[ $DJANGO_DEBUG -eq 0 ]]; then
  echo "Using production mode"
  python manage.py collectstatic --noinput
  gunicorn -w 4 --env DJANGO_SETTINGS_MODULE=_project.settings _project.wsgi -b 0.0.0.0:8000
else
  echo "Using development mode"
  python manage.py runserver 0.0.0.0:8000
fi
