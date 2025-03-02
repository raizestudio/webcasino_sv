from games.models import Game, GameCategory
from games.serializers import GameCategorySerializer, GameSerializer
from rest_framework.viewsets import ModelViewSet


class GameCategoryViewSet(ModelViewSet):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
