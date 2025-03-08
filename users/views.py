from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from auth_core.authentication import APIKeyAuthentication
from auth_core.permissions import IsAdminOrAPIKeyUser
from knox.auth import TokenAuthentication

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrAPIKeyUser,)
    authentication_classes = (APIKeyAuthentication, TokenAuthentication)
