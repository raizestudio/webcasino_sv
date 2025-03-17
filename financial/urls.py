from rest_framework.routers import DefaultRouter

from financial.views import (
    CurrencyViewSet,
    ExchangeViewSet,
    FinancialApiProviderViewSet,
    PoolViewSet,
    WalletViewSet,
)

router = DefaultRouter()
router.register("currencies", CurrencyViewSet)
router.register("wallets", WalletViewSet)
router.register("pools", PoolViewSet)
router.register("exchanges", ExchangeViewSet)
router.register("financial-api-providers", FinancialApiProviderViewSet)

urlpatterns = router.urls
