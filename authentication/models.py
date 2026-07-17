from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # AbstractUser gère déjà le username, password, email, etc.
    # On le laisse vide comme recommandé pour la configuration initiale
    pass
