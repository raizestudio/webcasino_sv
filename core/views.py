from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.models import Menu
from core.serializers import MenuSerializer


class RootView(APIView):
    def get(self, request):

        response = {
            "detail": "Should i call you mistah?",
            "api_version": settings.API_VERSION,
        }
        return Response(response)


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = (IsAdminOrAPIKeyUser,)
    # authentication_classes = (APIKeyAuthentication, TokenAuthentication)
