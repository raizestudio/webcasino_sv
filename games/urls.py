from rest_framework.routers import DefaultRouter

from games.views import GameCategoryViewSet, GameViewSet

router = DefaultRouter()
router.register(r"categories", GameCategoryViewSet)
router.register(r"", GameViewSet)


urlpatterns = router.urls
