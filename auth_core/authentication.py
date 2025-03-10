from django.core.exceptions import ValidationError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from auth_core.models import APIKey


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("x-api-key")
        print(f"API KEY: {api_key}")
        if not api_key:
            return None

        try:
            print(f"Will try to get API Key")
            _api_key = APIKey.objects.get(key=api_key)

        except APIKey.DoesNotExist:
            raise AuthenticationFailed("Invalid API Key")

        except ValidationError:
            raise AuthenticationFailed("Invalid API Key")
        return (_api_key.client, None)
