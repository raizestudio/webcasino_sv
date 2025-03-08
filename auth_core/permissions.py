from rest_framework.permissions import BasePermission

class IsAuthenticatedOrAPIKeyUser(BasePermission):
    """
    Allows access to:
    - Authenticated users (Django users with is_staff=True)
    - API clients (authenticated via APIKeyAuthentication)
    """

    def has_permission(self, request, view):
        user = request.user
        
        print(f"In IsAuthenticatedOrAPIKeyUser")
        print(f"User: {user}")
        # if user.is_anonymous:
        #     return False
        # print(f"User: {user}")
        # If user is a Django user, check if they are admin
        if hasattr(user, "is_authenticated"):
            print(f"User is authenticated: {user.is_authenticated}")
            return user.is_authenticated
        
        print(f"user api key: {user.api_key}")
        # If user is an APIKeyClient, allow access
        if hasattr(user, "api_key"):  # Adjust this based on your APIKeyClient model
            print(f"User is API Key Client: {user.api_key}")
            return True

        return False
    
class IsAdminOrAPIKeyUser(BasePermission):
    """
    Allows access to:
    - Admin users (Django users with is_staff=True)
    - API clients (authenticated via APIKeyAuthentication)
    """

    def has_permission(self, request, view):
        user = request.user
        
        # if user.is_anonymous:
        #     return False
        # print(f"User: {user}")
        # If user is a Django user, check if they are admin
        if hasattr(user, "is_staff"):
            return user.is_staff
        
        # If user is an APIKeyClient, allow access
        if hasattr(user, "api_key"):  # Adjust this based on your APIKeyClient model
            return True

        return False
