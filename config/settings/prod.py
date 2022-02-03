from decouple import config
import django_on_heroku

from .base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['steamscraperwebsite.herokuapp.com']

django_on_heroku.settings(locals(), staticfiles=False)