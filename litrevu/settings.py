"""
Paramètres Django pour le projet litrevu_project.

Généré par 'django-admin startproject' avec Django 5.0.14.
"""

import os
from pathlib import Path

# Construction des chemins à l'intérieur du projet
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-becek-09x994cy4jm3s58^pdw2yz43r407q2))_y_eb@+ghf=7"

DEBUG = True

ALLOWED_HOSTS = []

# Applications installées
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "authentication",
    "litrevu",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "litrevu.urls"

TEMPLATES = [
    {
        # Attention au '.django' au milieu :
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

WSGI_APPLICATION = "litrevu.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "authentication.User"
LOGIN_URL = "login"

# Configuration des fichiers médias
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Affichage des e-mails de réinitialisation de mot de passe dans le terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"