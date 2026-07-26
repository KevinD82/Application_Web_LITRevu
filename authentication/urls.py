from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_page, name="root_login"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.signup_page, name="signup"),
    path("home/", views.home, name="home"),
    path("posts/", views.posts, name="posts"),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    
    # Tickets
    path("ticket/create/", views.ticket_create, name="ticket_create"),
    path("ticket/<int:ticket_id>/update/", views.ticket_update, name="ticket_update"),
    path("ticket/<int:ticket_id>/delete/", views.ticket_delete, name="ticket_delete"),
    
    # Critiques
    path("review/create/", views.review_create, name="review_create"),
    path("ticket/<int:ticket_id>/reply/", views.review_create_reply, name="review_create_reply"),
    path("review/<int:review_id>/update/", views.review_update, name="review_update"),
    path("review/<int:review_id>/delete/", views.review_delete, name="review_delete"),
]