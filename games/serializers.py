from card_games.models import Poker, TexasHoldEm
from card_games.serializers import PokerSerializer, TexasHoldEmSerializer
from games.models import Game, GameCategory
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers


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

    # POLYMORPHIC_SERIALIZERS = {
    #     Poker: PokerSerializer,
    #     TexasHoldEm: TexasHoldEmSerializer,
    # }

    # def get_serializer(self, *args, **kwargs):
    #     kwargs["context"] = self.get_serializer_context()
    #     kwargs["expand"] = self.request.query_params.getlist("expand")
    #     return super().get_serializer(*args, **kwargs)

    # def to_representation(self, instance):
    #     expand_fields = self.context.get("expand", [])
    #     print("Expand fields:", expand_fields)  # Debugging
    #     serializer_class = self.POLYMORPHIC_SERIALIZERS.get(type(instance), GameSerializer)
    #     serializer = serializer_class(instance, context=self.context, expand=expand_fields)
    #     return serializer.data
