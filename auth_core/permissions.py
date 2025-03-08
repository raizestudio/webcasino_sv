from rest_framework.permissions import BasePermission

class IsAdminOrAPIKeyUser(BasePermission):
    """
    Allows access to:
    - Admin users (Django users with is_staff=True)
    - API clients (authenticated via APIKeyAuthentication)
    """

    def has_permission(self, request, view):
        user = request.user
        
        print(f"User: {user}")
        print(f"User: {user.api_key}")
        # If user is a Django user, check if they are admin
        if hasattr(user, "is_staff"):
            return user.is_staff
        
        # If user is an APIKeyClient, allow access
        if hasattr(user, "api_key"):  # Adjust this based on your APIKeyClient model
            return True

        return False
