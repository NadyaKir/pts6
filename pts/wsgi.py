"""
WSGI config for pts project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pts.settings.production")

if os.environ.get("DJANGO_SETTINGS_MODULE") == "pts.settings.production":
    from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
    application = Sentry(get_wsgi_application())
else:
    get_wsgi_application()
    
