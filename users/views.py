from django_filters.rest_framework import DjangoFilterBackend
from knox.auth import TokenAuthentication
from rest_framework import filters, viewsets

from auth_core.authentication import APIKeyAuthentication
from auth_core.permissions import IsAdminOrAPIKeyUser
from users.models import PlayerProfile, User
from users.serializers import PlayerProfileSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related("player_profile")
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["username", "email", "is_active"]

    permission_classes = (IsAdminOrAPIKeyUser,)
    authentication_classes = (APIKeyAuthentication, TokenAuthentication)


class PlayerProfileViewSet(viewsets.ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    permission_classes = (IsAdminOrAPIKeyUser,)
    authentication_classes = (APIKeyAuthentication, TokenAuthentication)
