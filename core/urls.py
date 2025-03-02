from core.views import RootView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("", RootView.as_view()),
    path("admin/", admin.site.urls),
    # path("auth/login/", LoginView.as_view()),
    # path("auth/logout/", LogoutView.as_view()),
    # path("auth/logout-all/", LogoutAllView.as_view()),
    # path("auth/", include("knox.urls")),
    path("auth/", include("auth.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("users/", include("users.urls")),
    path("games/", include("games.urls")),
    path("card-games/", include("card_games.urls")),
]
