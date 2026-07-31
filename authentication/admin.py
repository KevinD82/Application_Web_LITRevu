from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import User  # Ajustez l'import si UserFollows est ici


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Conserve l'affichage classique et complet de la gestion des utilisateurs Django
    pass