#!/bin/sh

# Aplica migraciones existentes automáticamente
python manage.py migrate --noinput

# Arranca Gunicorn
exec gunicorn portafolio.wsgi:application --bind 0.0.0.0:8000
