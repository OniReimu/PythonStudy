#!/bin/bash

django-admin.py startproject composedjango /etc/service/django/

cp /code/settings.py /etc/service/django/composedjango/settings.py

python /etc/service/django/manage.py migrate
