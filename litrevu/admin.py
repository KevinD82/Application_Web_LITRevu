from django.contrib import admin

from litrevu.models import Review, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "time_created")
    search_fields = ("title", "description")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("headline", "ticket", "user", "rating", "time_created")
    search_fields = ("headline", "body")