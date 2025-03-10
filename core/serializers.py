from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from core.models import Menu


class MenuSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {"parent": {"required": False}}
        expandable_fields = {
            "parent": "core.serializers.MenuSerializer",
        }
