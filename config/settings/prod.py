import django_on_heroku

from .base import *




SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['steamscraperwebsite.herokuapp.com']

django_on_heroku.settings(locals(), staticfiles=False)