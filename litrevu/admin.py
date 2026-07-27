from django.contrib import admin

from litrevu.models import Review, Ticket


# Enregistrement et configuration du modèle Ticket dans l'interface d'administration
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des tickets (titre, auteur, date de création)
    list_display = ("title", "user", "time_created")
    # Champs sur lesquels la barre de recherche textuelle de l'admin va opérer
    search_fields = ("title", "description")


# Enregistrement et configuration du modèle Review dans l'interface d'administration
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des critiques (titre, ticket associé, auteur, note, date)
    list_display = ("headline", "ticket", "user", "rating", "time_created")
    # Champs textuels indexés par la barre de recherche de l'admin
    search_fields = ("headline", "body")