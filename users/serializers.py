from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from users.models import PlayerProfile, User, UserPreferences, UserSecurity


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # Include password
        extra_kwargs = {"password": {"write_only": True}}  # Prevent password from being returned
        expandable_fields = {
            "player_profile": "users.serializers.PlayerProfileSerializer",
            "preferences": "users.serializers.UserPreferencesSerializer",
            "security": "users.serializers.UserSecuritySerializer",
        }
        # depth = 1

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)  # Hash the password before saving
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)  # Hash the password before saving
            user.save()
        return user


class UserPreferencesSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = UserPreferences
        fields = "__all__"
        expandable_fields = {
            "user": UserSerializer,
        }


class UserSecuritySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = UserSecurity
        fields = "__all__"
        expandable_fields = {
            "user": UserSerializer,
        }


class PlayerProfileSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = "__all__"
        expandable_fields = {
            "user": UserSerializer,
        }
