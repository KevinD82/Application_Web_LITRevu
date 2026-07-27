import django.urls
from django.contrib import admin

from authentication import views as auth_views

urlpatterns = [
    django.urls.path('admin/', admin.site.urls),
    
    # Authentification & Vues principales
    django.urls.path('', auth_views.login_page, name='login'),
    django.urls.path('logout/', auth_views.logout_user, name='logout'),
    django.urls.path('signup/', auth_views.signup_page, name='signup'),
    django.urls.path('home/', auth_views.home, name='home'),
    django.urls.path('posts/', auth_views.posts, name='posts'),
    django.urls.path('subscriptions/', auth_views.subscriptions, name='subscriptions'),
    django.urls.path('subscriptions/unsubscribe/<int:follow_id>/', auth_views.unsubscribe, name='unsubscribe'),  # <-- Ajouté pour corriger l'erreur
    
    # Routes Tickets
    django.urls.path('ticket/create/', auth_views.ticket_create, name='ticket_create'),
    django.urls.path('ticket/<int:ticket_id>/update/', auth_views.ticket_update, name='ticket_update'),
    django.urls.path('ticket/<int:ticket_id>/delete/', auth_views.ticket_delete, name='ticket_delete'),
    
    # Routes Critiques
    django.urls.path('review/create/', auth_views.review_create, name='review_create'),
    django.urls.path('ticket/<int:ticket_id>/reply/', auth_views.review_create_reply, name='review_create_reply'),
    django.urls.path('review/create/from-ticket/<int:ticket_id>/', auth_views.review_create_reply, name='review_create_from_ticket'), # Alias au cas où le template l'utilise
    django.urls.path('review/<int:review_id>/update/', auth_views.review_update, name='review_update'),
    django.urls.path('review/<int:review_id>/delete/', auth_views.review_delete, name='review_delete'),
]