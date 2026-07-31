from django.contrib import admin

from litrevu.models import (  # Ajustez selon l'emplacement de vos modèles
    Review,
    Ticket,
    UserFollows,
)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'time_created')
    search_fields = ('title', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'rating', 'user', 'time_created')
    search_fields = ('headline', 'body')

@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')