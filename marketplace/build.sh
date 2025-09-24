#!/usr/bin/env bash 
set -o errexit 
pip install -r requirements.txt 
cd marketplace 
python manage.py migrate 
python manage.py collectstatic --no-input 
