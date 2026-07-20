from django.contrib import admin
from django.urls import path, include
from litrevu import views as litrevu_views
from authentication import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", auth_views.login_page, name="root_login"),
    path("", include("authentication.urls")),
    path("home/", litrevu_views.home, name="home"),
]
