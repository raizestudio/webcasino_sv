from financial.models import Currency
from financial.serializers import CurrencySerializer
from rest_framework.viewsets import ModelViewSet


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
