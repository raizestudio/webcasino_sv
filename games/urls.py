from games.views import GameViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", GameViewSet)


urlpatterns = router.urls
