from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet, basename="users")
urlpatterns = router.urls
