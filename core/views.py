from rest_framework.response import Response
from rest_framework.views import APIView


class RootView(APIView):
    def get(self, request):
        return Response({"message": "Should i call you mistah?"})
