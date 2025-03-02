from auth.views import LoginView, LogoutAllView, LogoutView
from django.urls import path

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("logout-all/", LogoutAllView.as_view()),
]
