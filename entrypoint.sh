#!/bin/sh

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Applying database migrations"
python manage.py migrate

echo "Starting Gunicorn"
exec gunicorn Shteki.wsgi:application --bind 0.0.0.0:8000 --workers 4
