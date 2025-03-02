from card_games.models import Deck, Poker, TexasHoldEm
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = "__all__"


class PokerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Poker
        fields = "__all__"


class TexasHoldEmSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TexasHoldEm
        fields = "__all__"


# class TexasHoldEmSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TexasHoldEm
#         fields = "__all__"
