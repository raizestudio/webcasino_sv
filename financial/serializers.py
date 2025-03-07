from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from financial.models import Currency, Wallet


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class WalletSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"
        expandable_fields = {
            "currency": CurrencySerializer,
            "user": "users.serializers.UserSerializer",
        }
