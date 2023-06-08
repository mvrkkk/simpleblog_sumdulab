#!/bin/bash

python3 /app/manage.py makemigrations --no-input
python3 /app/manage.py migrate --no-input
python3 /app/manage.py runserver
