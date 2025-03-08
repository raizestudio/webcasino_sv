from django.urls import path

from auth_core.views import AuthView, LoginView, LogoutAllView, LogoutView

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("user/", AuthView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("logout-all/", LogoutAllView.as_view()),
]
