from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutAllView as KnoxLogoutAllView
from knox.views import LogoutView as KnoxLogoutView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.serializers import CustomAuthTokenSerializer
from users.serializers import UserSerializer


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

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
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        return Response({"user": UserSerializer(user).data})


class LogoutView(KnoxLogoutView):
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        return super().post(request, format=None)


class LogoutAllView(KnoxLogoutAllView):
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        return super().post(request, format=None)
