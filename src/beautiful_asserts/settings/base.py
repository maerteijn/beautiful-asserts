import os

import environ

env = environ.Env()
environ.Env.read_env(".env")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CACHES = {"default": env.cache(default="dummycache://")}

DATABASES = {"default": env.db_url(default="sqlite:///beautiful-asserts.db")}

DEBUG = env.bool("DEBUG", default=True)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_FROM_EMAIL = env.str(
    "DEFAULT_FROM_EMAIL", default="Beautiful Asserts <no-reply@beautiful-asserts.com>"
)

EMAIL_HOST = env.str("EMAIL_HOST", default="localhost")
EMAIL_PORT = env.int("EMAIL_PORT", default=1025)

INSTALLED_APPS = [
    "beautiful_asserts",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.auth",
]

LANGUAGES = [
    ("en", "English"),
]

LANGUAGE_CODE = "en"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"  # noqa
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "null": {"class": "logging.NullHandler"},
    },
    "loggers": {
        "beautiful_asserts": {"level": "INFO", "propagate": True},
        "wagtail": {"level": "INFO", "propagate": True},
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

MEDIA_URL = env.str("MEDIA_URL", default="/media/")
MEDIA_ROOT = os.path.join(BASE_DIR, "public/media")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = env.str("ROOT_URLCONF", default="beautiful_asserts.urls")

SECRET_KEY = env.str("SECRET_KEY", default="XTKCe-gTKCTNAt23N7W!ka*e.R4-_QY@jQvdPBEm@rEFHqTi44eW@DaZH4vCrudqk9NN8pGUKXVw-Tq2")

STATIC_URL = env.str("STATIC_URL", default="/static/")
STATIC_ROOT = os.path.join(BASE_DIR, "public/static")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = True
USE_TZ = True

WSGI_APPLICATION = "beautiful_asserts.wsgi.application"
