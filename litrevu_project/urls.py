from django.contrib import admin
from django.urls import path, include
from authentication import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentification & Vues principales
    path('', auth_views.login_page, name='login'),
    path('logout/', auth_views.logout_user, name='logout'),
    path('signup/', auth_views.signup_page, name='signup'),
    path('home/', auth_views.home, name='home'),
    path('posts/', auth_views.posts, name='posts'),
    path('subscriptions/', auth_views.subscriptions, name='subscriptions'),
    
    # Routes Tickets
    path('ticket/create/', auth_views.ticket_create, name='ticket_create'),
    path('ticket/<int:ticket_id>/update/', auth_views.ticket_update, name='ticket_update'),  # <-- Manquait ici
    path('ticket/<int:ticket_id>/delete/', auth_views.ticket_delete, name='ticket_delete'),  # <-- Manquait ici
    
    # Routes Critiques
    path('review/create/', auth_views.review_create, name='review_create'),
    path('ticket/<int:ticket_id>/reply/', auth_views.review_create_reply, name='review_create_reply'),
    path('review/<int:review_id>/update/', auth_views.review_update, name='review_update'),  # <-- Manquait ici
    path('review/<int:review_id>/delete/', auth_views.review_delete, name='review_delete'),  # <-- Manquait ici
]