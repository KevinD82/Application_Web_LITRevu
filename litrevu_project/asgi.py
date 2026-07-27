"""
Configuration ASGI pour le projet litrevu_project.

Il expose l'objet appelable ASGI en tant que variable de module nommée ``application``.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Définition de la variable d'environnement par défaut pointant vers le module de configuration du projet Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'litrevu_project.settings')

# Récupération de l'application ASGI standard de Django pour gérer les requêtes asynchrones
application = get_asgi_application()