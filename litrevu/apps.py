from django.apps import AppConfig


# Configuration de l'application 'litrevu'
class LitrevuConfig(AppConfig):
    # Définition du type de clé primaire par défaut pour les modèles de cette application (entier long 64 bits)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nom technique de l'application Django, utilisé notamment dans INSTALLED_APPS
    name = 'litrevu'