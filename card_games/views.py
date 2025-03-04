from card_games.models import Deck, Poker
from card_games.serializers import DeckSerializer
from rest_framework.viewsets import ModelViewSet


class DeckViewSet(ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


# class TexasHoldEmViewSet(ModelViewSet):
#     queryset = TexasHoldEm.objects.all()
#     serializer_class = TexasHoldEmSerializer
