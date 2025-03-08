from django.contrib.auth import authenticate
from rest_framework import serializers

from auth_core.models import APIKey, APIKeyClient


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(trim_whitespace=False)
    password = serializers.CharField(trim_whitespace=False)

    def validate(self, attrs):
        print(f"IS VALIDATING")
        email = attrs.get("email")
        password = attrs.get("password")

        print(f"Email: {email}")
        print(f"Password: {password}")
        if email and password:
            print(f"Try authenticate")
            user = authenticate(email=email, password=password)
            print(f"User: {user}")
            if not user:
                raise serializers.ValidationError(
                    "Unable to log in with provided credentials.", code="authorization"
                )
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        attrs["user"] = user
        return attrs


class APIKeyClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKeyClient
        fields = "__all__"


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = "__all__"
