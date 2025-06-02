from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Mantém o DATABASES herdado do base.py (que já usa PostgreSQL via .env)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
