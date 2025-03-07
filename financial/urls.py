from rest_framework.routers import DefaultRouter

from financial.views import CurrencyViewSet, WalletViewSet

router = DefaultRouter()
router.register("currencies", CurrencyViewSet)
router.register("wallets", WalletViewSet)

urlpatterns = router.urls
