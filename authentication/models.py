from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # AbstractUser gère déjà username, password, email, etc.
    pass
