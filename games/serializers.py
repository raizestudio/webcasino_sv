from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from games.models import Game, GameCategory


class GameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCategory
        fields = "__all__"


class GameSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
        expandable_fields = {
            "category": GameCategorySerializer,
        }
