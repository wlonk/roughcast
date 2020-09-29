# ABSOLUTELY MINIMIZE WHAT YOU PUT IN HERE.

# This should ideally be *empty*, but failing that, there are a few
# things that should be in here: faked out email, faked out media
# storage, etc.


from .base import *  # noqa

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
