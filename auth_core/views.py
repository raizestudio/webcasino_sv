from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutAllView as KnoxLogoutAllView
from knox.views import LogoutView as KnoxLogoutView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# from rest_framework.authentication import TokenAuthentication
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from auth_core.serializers import CustomAuthTokenSerializer, APIKeyClientSerializer, APIKeySerializer
from users.serializers import UserSerializer
from auth_core.models import APIKey, APIKeyClient
from auth_core.permissions import IsAdminOrAPIKeyUser, IsAuthenticatedOrAPIKeyUser
from auth_core.authentication import APIKeyAuthentication

class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = CustomAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        # return super().post(request, format=None)

        knox_response = super().post(request, format=None).data
        user_data = UserSerializer(user).data

        return Response(
            {"token": knox_response["token"], "expiry": knox_response["expiry"], "user": user_data}
        )  # Add user info


class AuthView(APIView):
    permission_classes = (IsAuthenticatedOrAPIKeyUser,)
    authentication_classes = (APIKeyAuthentication, TokenAuthentication)

    def get(self, request, format=None):
        user = request.user
        
        if hasattr(user, "is_authenticated"):
            return Response({"user": UserSerializer(user).data})
        
        if hasattr(user, "api_key"):
            return Response({"api_key_client": APIKeyClientSerializer(user).data})

        return Response({"detail": "User or ApiKeyClient not found"})

class LogoutView(KnoxLogoutView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        return super().post(request, format=None)


class LogoutAllView(KnoxLogoutAllView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        return super().post(request, format=None)


class APIKeyClientViewSet(ModelViewSet):
    queryset = APIKeyClient.objects.all()
    serializer_class = APIKeyClientSerializer
    permission_classes = (IsAdminUser,)
    

class APIKeyViewSet(ModelViewSet):
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer
    permission_classes = (IsAdminUser,)

    