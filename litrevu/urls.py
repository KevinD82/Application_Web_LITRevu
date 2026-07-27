import django.urls
from django.contrib import admin

from authentication import views as auth_views

urlpatterns = [
    # Route d'accès au panneau d'administration de Django
    django.urls.path('admin/', admin.site.urls),
    
    # --- Authentification & Vues principales ---
    # Page de connexion (racine du site)
    django.urls.path('', auth_views.login_page, name='login'),
    # Route de déconnexion de l'utilisateur
    django.urls.path('logout/', auth_views.logout_user, name='logout'),
    # Page de création d'un nouveau compte (inscription)
    django.urls.path('signup/', auth_views.signup_page, name='signup'),
    # Page du flux principal réunissant les tickets et critiques
    django.urls.path('home/', auth_views.home, name='home'),
    # Page listant l'historique des publications de l'utilisateur connecté
    django.urls.path('posts/', auth_views.posts, name='posts'),
    # Page de gestion des abonnements et des abonnés
    django.urls.path('subscriptions/', auth_views.subscriptions, name='subscriptions'),
    # Route permettant de se désabonner d'un utilisateur via l'ID du lien de suivi
    django.urls.path('subscriptions/unsubscribe/<int:follow_id>/', auth_views.unsubscribe, name='unsubscribe'),
    
    # --- Routes Tickets ---
    # Route pour créer un nouveau ticket (demande de critique)
    django.urls.path('ticket/create/', auth_views.ticket_create, name='ticket_create'),
    # Route pour modifier un ticket existant repéré par son ID
    django.urls.path('ticket/<int:ticket_id>/update/', auth_views.ticket_update, name='ticket_update'),
    # Route pour supprimer un ticket existant
    django.urls.path('ticket/<int:ticket_id>/delete/', auth_views.ticket_delete, name='ticket_delete'),
    
    # --- Routes Critiques ---
    # Route pour créer une critique et son ticket associé en une seule étape
    django.urls.path('review/create/', auth_views.review_create, name='review_create'),
    # Route pour répondre à un ticket existant en créant une critique
    django.urls.path('ticket/<int:ticket_id>/reply/', auth_views.review_create_reply, name='review_create_reply'),
    # Alias de secours pour la création de critique depuis un ticket existant
    django.urls.path('review/create/from-ticket/<int:ticket_id>/', auth_views.review_create_reply, name='review_create_from_ticket'),
    # Route pour modifier une critique existante
    django.urls.path('review/<int:review_id>/update/', auth_views.review_update, name='review_update'),
    # Route pour supprimer une critique existante
    django.urls.path('review/<int:review_id>/delete/', auth_views.review_delete, name='review_delete'),
]