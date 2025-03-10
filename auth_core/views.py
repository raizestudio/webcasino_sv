import requests
from django.conf import settings
from django.contrib.auth import login

# from rest_framework.authentication import TokenAuthentication
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutAllView as KnoxLogoutAllView
from knox.views import LogoutView as KnoxLogoutView
from rest_framework import request, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from auth_core.authentication import APIKeyAuthentication
from auth_core.models import APIKey, APIKeyClient, Session
from auth_core.permissions import IsAdminOrAPIKeyUser, IsAuthenticatedOrAPIKeyUser
from auth_core.serializers import (
    APIKeyClientSerializer,
    APIKeySerializer,
    CustomAuthTokenSerializer,
    SessionSerializer,
)
from geo.models import Country
from users.serializers import UserSerializer


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = CustomAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        # return super().post(request, format=None)

        knox_response = super().post(request, format=None).data
        user_data = UserSerializer(user, context={"request": request}).data

        return Response({"token": knox_response["token"], "expiry": knox_response["expiry"], "user": user_data})  # Add user info


class AuthView(APIView):
    permission_classes = (IsAuthenticatedOrAPIKeyUser,)
    authentication_classes = (APIKeyAuthentication, TokenAuthentication)

    def get(self, request, format=None):
        user = request.user

        if hasattr(user, "is_authenticated"):
            return Response({"user": UserSerializer(user, context={"request": request}).data})

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


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    @action(detail=False, methods=["get"], url_path="ip-info")
    def get_session_with_ip(self, request):
        """Fetches session info with IP details"""
        client_id = request.query_params.get("client_id")

        if not client_id:
            return Response({"error": "client_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            _session = Session.objects.get(ip=client_id)
            return Response(SessionSerializer(_session).data, status=status.HTTP_200_OK)

        except Session.DoesNotExist:
            ...

        # Fetch IP info from external API
        ip_api_url = f"{settings.IP_INFO_URL}json/{client_id}"
        try:
            response = requests.get(ip_api_url)
            response.raise_for_status()
            ip_data = response.json()
            print(ip_data["ipAddress"])
            _session = Session.objects.create(
                ip=ip_data["ipAddress"],
            )

            # _session.save()
        except requests.RequestException as e:
            return Response({"error": "Failed to fetch IP data", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Optionally store the IP info in the session (if needed)
        # session.ip_info = ip_data  # Make sure `ip_info` exists as a JSONField in your model
        # session.save()

        return Response(SessionSerializer(_session).data, status=status.HTTP_200_OK)
        # return Response(ip_data, status=status.HTTP_200_OK)
