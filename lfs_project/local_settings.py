# -*- coding: utf-8 -*-

# python imports
import os

DIRNAME = os.path.dirname(__file__)

DEFAULT_FROM_EMAIL = 'your_email@domain.com'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DIRNAME + 'lfs.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en'


EMAIL_HOST = "localhost"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""