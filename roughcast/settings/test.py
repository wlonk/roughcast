from .base import *  # noqa

# Suppress real email sending in tests!
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
