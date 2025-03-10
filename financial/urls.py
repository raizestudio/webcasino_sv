from rest_framework.routers import DefaultRouter

from financial.views import CurrencyViewSet, PoolViewSet, WalletViewSet

router = DefaultRouter()
router.register("currencies", CurrencyViewSet)
router.register("wallets", WalletViewSet)
router.register("pools", PoolViewSet)

urlpatterns = router.urls
