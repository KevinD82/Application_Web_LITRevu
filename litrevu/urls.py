import django.urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as django_auth_views

from litrevu import views as auth_views

urlpatterns = [
    # Route d'accès au panneau d'administration
    django.urls.path('admin/', admin.site.urls),
    
    # --- Authentification & Vues principales ---
    django.urls.path('', auth_views.login_page, name='login'),
    django.urls.path('index/', auth_views.login_page, name='login'),
    django.urls.path('logout/', auth_views.logout_user, name='logout'),
    django.urls.path('signup/', auth_views.signup_page, name='signup'),
    django.urls.path('home/', auth_views.home, name='home'),
    django.urls.path('posts/', auth_views.posts, name='posts'),
    django.urls.path('subscriptions/', auth_views.subscriptions, name='subscriptions'),
    django.urls.path('subscriptions/unsubscribe/<int:follow_id>/', auth_views.unsubscribe, name='unsubscribe'),
    
    # --- Mot de passe oublié (Formulaire standard par e-mail) ---
    django.urls.path(
        'password-reset/', 
        django_auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'), 
        name='password_reset'
    ),
    django.urls.path(
        'password-reset/done/', 
        django_auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), 
        name='password_reset_done'
    ),
    django.urls.path(
        'password-reset-confirm/<uidb64>/<token>/', 
        django_auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'), 
        name='password_reset_confirm'
    ),
    django.urls.path(
        'password-reset-complete/', 
        django_auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), 
        name='password_reset_complete'
    ),

    # --- Routes Tickets ---
    django.urls.path('ticket/create/', auth_views.ticket_create, name='ticket_create'),
    django.urls.path('ticket/<int:ticket_id>/update/', auth_views.ticket_update, name='ticket_update'),
    django.urls.path('ticket/<int:ticket_id>/delete/', auth_views.ticket_delete, name='ticket_delete'),
    
    # --- Routes Critiques ---
    django.urls.path('review/create/', auth_views.review_create, name='review_create'),
    django.urls.path('ticket/<int:ticket_id>/reply/', auth_views.review_create_reply, name='review_create_reply'),
    django.urls.path('review/create/from-ticket/<int:ticket_id>/', auth_views.review_create_reply, name='review_create_from_ticket'),
    django.urls.path('review/<int:review_id>/update/', auth_views.review_update, name='review_update'),
    django.urls.path('review/<int:review_id>/delete/', auth_views.review_delete, name='review_delete'),
]

# Servir les fichiers médias (images) durant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)