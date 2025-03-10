from django.urls import path
from rest_framework.routers import DefaultRouter

from auth_core.views import (
    AuthView,
    LoginView,
    LogoutAllView,
    LogoutView,
    SessionViewSet,
)

router = DefaultRouter()
router.register("sessions", SessionViewSet)

urlpatterns = router.urls
urlpatterns += [
    path("login/", LoginView.as_view()),
    path("user/", AuthView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("logout-all/", LogoutAllView.as_view()),
]
