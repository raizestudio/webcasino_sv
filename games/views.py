from games.models import Game
from games.serializers import GameSerializer
from rest_framework.viewsets import ModelViewSet


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
