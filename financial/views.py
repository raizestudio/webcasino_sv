from rest_framework.viewsets import ModelViewSet

from financial.models import Currency, Pool, Wallet
from financial.serializers import CurrencySerializer, PoolSerializer, WalletSerializer


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class PoolViewSet(ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
