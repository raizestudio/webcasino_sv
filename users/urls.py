from rest_framework.routers import DefaultRouter

from users.views import PlayerProfileViewSet, UserViewSet

router = DefaultRouter()
router.register(r"player-profiles", PlayerProfileViewSet, basename="player-profiles")
router.register(r"", UserViewSet, basename="users")
urlpatterns = router.urls
