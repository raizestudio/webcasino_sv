from games.views import GameCategoryViewSet, GameViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"categories", GameCategoryViewSet)
router.register(r"", GameViewSet)


urlpatterns = router.urls
