from rest_framework.viewsets import ModelViewSet

from games.models import Game, GameCategory
from games.serializers import GameCategorySerializer, GameSerializer


class GameCategoryViewSet(ModelViewSet):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # def get_serializer(self, *args, **kwargs):
    #     kwargs["context"] = self.get_serializer_context()
    #     kwargs["context"]["expand"] = self.request.query_params.getlist("expand")  # ✅ Fix here
    #     print(f"Expand query params: {kwargs['context']['expand']}")  # Debugging
    #     return super().get_serializer(*args, **kwargs)
