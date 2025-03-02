from card_games.models import Deck, TexasHoldEm
from card_games.serializers import DeckSerializer, TexasHoldEmSerializer
from rest_framework.viewsets import ModelViewSet


class DeckViewSet(ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


class TexasHoldEmViewSet(ModelViewSet):
    queryset = TexasHoldEm.objects.all()
    serializer_class = TexasHoldEmSerializer
