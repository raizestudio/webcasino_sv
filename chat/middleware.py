from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from knox.auth import TokenAuthentication


@database_sync_to_async
def get_user_from_token(token):
    """
    Retrieves the user associated with the given Knox token.
    """
    auth = TokenAuthentication()
    try:
        user, _ = auth.authenticate_credentials(token.encode())
        return user
    except Exception:
        return AnonymousUser()


class KnoxAuthMiddleware:
    """
    Custom authentication middleware for Django Channels using Knox tokens.
    Extracts the token from the query string or headers.
    """

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # Extract token from query string
        query_string = parse_qs(scope["query_string"].decode())
        token = query_string.get("token", [None])[0]

        # If token is found, authenticate user
        if token:
            scope["user"] = await get_user_from_token(token)
        else:
            scope["user"] = AnonymousUser()

        return await self.inner(scope, receive, send)


# Wrapper function to use with ASGI applications
def KnoxAuthMiddlewareStack(inner):
    return KnoxAuthMiddleware(inner)
