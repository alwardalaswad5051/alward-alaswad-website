"""
Django settings for alward_site project.
"""

from pathlib import Path
import os


# ---------------------------------------------------------
# BASE DIRECTORY
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------
# SECURITY
# ---------------------------------------------------------

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-development-only-change-this-before-production",
)

DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "DJANGO_ALLOWED_HOSTS",
        "127.0.0.1,localhost",
    ).split(",")
    if host.strip()
]

# ---------------------------------------------------------
# APPLICATIONS
# ---------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "website",
]


# ---------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------

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

# ---------------------------------------------------------
# URLS / WSGI
# ---------------------------------------------------------

ROOT_URLCONF = "alward_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "alward_site.wsgi.application"


# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ---------------------------------------------------------
# INTERNATIONALIZATION
# ---------------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dubai"

USE_I18N = True

USE_TZ = True


# ---------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "website" / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ---------------------------------------------------------
# MEDIA FILES
# ---------------------------------------------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ---------------------------------------------------------
# EMAIL
# ---------------------------------------------------------

MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "OPTIONS": {
            "host": os.environ.get("EMAIL_HOST", ""),
            "port": int(os.environ.get("EMAIL_PORT", "587")),
            "username": os.environ.get("EMAIL_USERNAME", ""),
            "password": os.environ.get("EMAIL_PASSWORD", ""),
            "use_tls": True,
            "timeout": 10,
        },
    },
}

DEFAULT_FROM_EMAIL = os.environ.get(
    "DEFAULT_FROM_EMAIL",
    "alwardlandscaping@gmail.com",
)


# ---------------------------------------------------------
# SECURITY SETTINGS
# ---------------------------------------------------------
# These remain disabled locally.
# We will enable them when HTTPS is configured on the
# production server.

SECURE_SSL_REDIRECT = (
    os.environ.get(
        "DJANGO_SECURE_SSL_REDIRECT",
        "False",
    ).lower()
    == "true"
)

SESSION_COOKIE_SECURE = (
    os.environ.get(
        "DJANGO_SESSION_COOKIE_SECURE",
        "False",
    ).lower()
    == "true"
)

CSRF_COOKIE_SECURE = (
    os.environ.get(
        "DJANGO_CSRF_COOKIE_SECURE",
        "False",
    ).lower()
    == "true"
)


# ---------------------------------------------------------
# HSTS
# ---------------------------------------------------------

SECURE_HSTS_SECONDS = int(
    os.environ.get(
        "DJANGO_SECURE_HSTS_SECONDS",
        "0",
    )
)

SECURE_HSTS_INCLUDE_SUBDOMAINS = (
    os.environ.get(
        "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS",
        "False",
    ).lower()
    == "true"
)

SECURE_HSTS_PRELOAD = (
    os.environ.get(
        "DJANGO_SECURE_HSTS_PRELOAD",
        "False",
    ).lower()
    == "true"
)


# ---------------------------------------------------------
# DEFAULT PRIMARY KEY
# ---------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"