#!/usr/bin/env python
"""Utilitaire de ligne de commande de Django pour les tâches administratives."""
import os
import sys


def main():
    """Exécute les tâches administratives (commandes manage.py comme runserver, migrate, etc.)."""
    # Définition de la variable d'environnement par défaut pointant vers le module de configuration du projet
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'litrevu.settings')
    try:
        # Importation de la fonction d'exécution des commandes Django depuis le module de gestion
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Lève une exception explicite si Django n'est pas installé ou si l'environnement virtuel n'est pas activé
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Exécution de la commande administrative passée en argument dans la ligne de commande (ex: python manage.py runserver)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()