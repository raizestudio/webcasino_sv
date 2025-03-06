from financial.views import CurrencyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("currencies", CurrencyViewSet)

urlpatterns = router.urls
