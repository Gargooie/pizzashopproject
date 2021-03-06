"""
WSGI config for pizzashopproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzashopproject.settings')

application = get_wsgi_application()

#use whitenoise package to serve static files on heroku
from whitenoise.django import DjangoWhiteNoise
application =DjangoWhiteNoise(application)