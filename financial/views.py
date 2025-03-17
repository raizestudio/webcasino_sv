from rest_framework.viewsets import ModelViewSet

from financial.models import Currency, Exchange, FinancialApiProvider, Pool, Wallet
from financial.serializers import (
    CurrencySerializer,
    ExchangeSerializer,
    FinancialApiProviderSerializer,
    PoolSerializer,
    WalletSerializer,
)


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class PoolViewSet(ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer


class ExchangeViewSet(ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


class FinancialApiProviderViewSet(ModelViewSet):
    queryset = FinancialApiProvider.objects.all()
    serializer_class = FinancialApiProviderSerializer
