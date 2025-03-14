from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from core.views import MenuViewSet, RootView

router = DefaultRouter()
router.register(r"menus", MenuViewSet)

urlpatterns = [
    path("", RootView.as_view(), name="root-view"),
    path("app/", include(router.urls)),
    path("admin/", admin.site.urls),
    # path("auth/login/", LoginView.as_view()),
    # path("auth/logout/", LogoutView.as_view()),
    # path("auth/logout-all/", LogoutAllView.as_view()),
    # path("auth/", include("knox.urls")),
    path("auth/", include("auth_core.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("users/", include("users.urls")),
    path("games/", include("games.urls")),
    path("financial/", include("financial.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
