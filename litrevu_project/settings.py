"""
Paramètres Django pour le projet litrevu_project.

Généré par 'django-admin startproject' avec Django 5.0.14.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/5.0/topics/settings/

Pour la liste complète des paramètres et de leurs valeurs, voir
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Construction des chemins à l'intérieur du projet de cette manière : BASE_DIR / 'sous_dossier'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Paramètres de démarrage rapide pour le développement - non adaptés pour la production
# Voir https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# AVERTISSEMENT DE SÉCURITÉ : gardez la clé secrète utilisée en production secrète !
SECRET_KEY = "django-insecure-becek-09x994cy4jm3s58^pdw2yz43r407q2))_y_eb@+ghf=7"

# AVERTISSEMENT DE SÉCURITÉ : ne lancez pas l'application avec DEBUG activé en production !
DEBUG = True

# Liste des noms de domaine ou hôtes autorisés à accéder à ce site (vide en mode dev local)
ALLOWED_HOSTS = []


# Définition des applications installées dans le projet Django
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Application personnalisée gérant l'authentification et les utilisateurs
    "authentication",
    # Application principale gérant les tickets, critiques et abonnements (LITRevu)
    "litrevu",
]

# Liste des middlewares (composants logiciels intermédiaires exécutés à chaque requête/réponse)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware", # Protection contre les attaques CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware", # Gestion de l'authentification des utilisateurs
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Chemin vers le fichier principal de routage des URLs du projet
ROOT_URLCONF = "litrevu_project.urls"

# Configuration des moteurs de templates HTML
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

# Chemin vers l'application WSGI pour le déploiement en production synchrone
WSGI_APPLICATION = "litrevu_project.wsgi.application"


# Base de données
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Configuration de la base de données par défaut (utilisant SQLite pour le développement)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Validation des mots de passe
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalisation
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# Langue par défaut du site (Français)
LANGUAGE_CODE = "fr-fr"

# Fuseau horaire par défaut du projet
TIME_ZONE = "UTC"

# Activation de l'internationalisation
USE_I18N = True

# Activation de la prise en compte des fuseaux horaires (Time Zones)
USE_TZ = True


# Fichiers statiques (CSS, JavaScript, Images du design)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Indique à Django de chercher des fichiers statiques supplémentaires à la racine du projet (dossier 'static/')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Type de champ par défaut pour les clés primaires auto-incrémentées (entiers longs 64 bits)
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Redéfinition du modèle utilisateur personnalisé pointant vers l'application 'authentication'
AUTH_USER_MODEL = "authentication.User"

# Nom ou chemin de l'URL vers laquelle rediriger les utilisateurs non connectés
LOGIN_URL = "login"

# Configuration pour les fichiers média (images téléversées par les utilisateurs, ex: couvertures de livres)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")