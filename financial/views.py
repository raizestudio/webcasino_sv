from rest_framework.viewsets import ModelViewSet

from financial.models import Currency, Wallet
from financial.serializers import CurrencySerializer, WalletSerializer


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Wallet.objects.filter(user=self.request.user)

        return super().get_queryset()
