"""
Django settings for roughcast project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from pathlib import Path

import dj_database_url

from .utils import boolish, env

# Build paths inside the project like this: str(BASE_DIR / "some_path")
BASE_DIR = Path(__file__).absolute().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")
HASHID_FIELD_SALT = env("HASHID_FIELD_SALT")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG", type_=boolish, default=False)
ALLOWED_HOSTS = [
    "roughcast.app",
    "roughcast.onrender.com",
]
if DEBUG:
    ALLOWED_HOSTS += [
        "localhost",
        "localhost:8000",
        "127.0.0.1",
        "127.0.0.1:8000",
        ".ngrok.io",
    ]

# HTTPS and HSTS
SECURE_SSL_REDIRECT = env("SECURE_SSL_REDIRECT", default=not DEBUG, type_=boolish)
SECURE_PROXY_SSL_HEADER = env(
    "SECURE_PROXY_SSL_HEADER",
    default="HTTP_X_FORWARDED_PROTO:https",
    type_=(lambda v: tuple(v.split(":", 1)) if (v is not None and ":" in v) else None),
)

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "roughcast",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
WSGI_APPLICATION = "roughcast.wsgi.application"
# @@@ WEBSOCKETS
# ASGI_APPLICATION = "roughcast.routing.application"
ROOT_URLCONF = "roughcast.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


ADMINS = (("Kit", "kit@transneptune.net"),)


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {"default": dj_database_url.config(default="postgres:///roughcast")}
AUTH_USER_MODEL = "roughcast.User"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "public"), str(BASE_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]


# Redis
# Used as the channels layer
# @@@ WEBSOCKETS
# REDIS_LOCATION = "{0}/{1}".format(
#     env("REDIS_URL", default="redis://localhost:6379"), 0
# )
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {"hosts": [REDIS_LOCATION]},
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
LOGIN_REDIRECT_URL = "/dashboard/"


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    # For things we make by hand:
    str(BASE_DIR / "static"),
    # For things Vue makes that are "assets":
    str(BASE_DIR / "dist" / "static"),
    # For things Vue makes that are "core":
    str(BASE_DIR / "dist"),
]
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

MEDIA_ROOT = str(BASE_DIR / "media")
MEDIA_URL = "/media/"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default=None)
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default=None)
AWS_S3_FILE_OVERWRITE = False
# We keep the file URLs in browser long enough that we can't rely on
# querystring auth:
AWS_QUERYSTRING_AUTH = False


# Email
DEFAULT_FROM_EMAIL = "no-reply@roughcast.app"
DEFAULT_SUPPORT_EMAIL = "support@roughcast.app"
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = env("SENDGRID_API_KEY", default=None)


# Django-registration
ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window
REGISTRATION_SALT = HASHID_FIELD_SALT


# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}
