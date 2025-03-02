from card_games.models import Deck, TexasHoldEm
from rest_framework import serializers


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = "__all__"


class TexasHoldEmSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexasHoldEm
        fields = "__all__"
