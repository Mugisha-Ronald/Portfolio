#!/usr/bin/env bash
# exit on error
set -o errexit

pip intall -r requirements.txt


#convert static assets
python manage.py collectstatic --no-input

#apply any outstanding database migrations
python manage.py migrate

