from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentication.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.login_page, name="root_login"),
    path("login/", authentication.views.login_page, name="login"),
    path("logout/", authentication.views.logout_user, name="logout"),
    path("signup/", authentication.views.signup_page, name="signup"),
    path("home/", authentication.views.home, name="home"),
    path("ticket/create/", authentication.views.ticket_create, name="ticket_create"),
    path("review/create/", authentication.views.review_create, name="review_create"),
]

# Servir les fichiers média téléchargés pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
