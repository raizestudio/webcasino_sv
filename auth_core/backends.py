from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, BaseBackend

User = get_user_model()
from auth_core.models import APIKey

class EmailBackend(ModelBackend):
    """Authenticate using email instead of username."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get("email")  # or username  # no username at the moment but can handle both
        if email is None:
            return None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        