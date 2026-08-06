# Importation du module d'administration de Django
from django.contrib import admin

# Importation des modèles de l'application litrevu que l'on souhaite gérer depuis l'interface admin
from litrevu.models import (
    Review,
    Ticket,
    UserFollows,
)


# Enregistrement et personnalisation de l'affichage du modèle Ticket dans l'admin
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # Colonnes affichées sous forme de tableau dans la liste des tickets
    list_display = ('title', 'user', 'time_created')
    # Champs sur lesquels il est possible d'effectuer une recherche textuelle
    search_fields = ('title', 'description')

# Enregistrement et personnalisation de l'affichage du modèle Review (Critique) dans l'admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des critiques (titre/en-tête, note, auteur, date)
    list_display = ('headline', 'rating', 'user', 'time_created')
    # Champs textuels ciblés par la barre de recherche de l'admin
    search_fields = ('headline', 'body')

# Enregistrement et personnalisation de l'affichage du modèle UserFollows (Abonnements) dans l'admin
@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    # Colonnes affichées pour voir quel utilisateur suit quel autre utilisateur
    list_display = ('user', 'followed_user')