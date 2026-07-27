"""
Configuration WSGI pour le projet litrevu_project.

Il expose l'objet appelable WSGI en tant que variable de module nommée ``application``.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Définition de la variable d'environnement par défaut pointant vers le module de configuration du projet Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'litrevu_project.settings')

# Récupération de l'application WSGI standard de Django pour gérer les requêtes web synchrones en production
application = get_wsgi_application()