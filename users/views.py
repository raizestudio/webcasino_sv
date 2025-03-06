from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
