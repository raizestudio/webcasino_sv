import logging

logger = logging.getLogger("auth_core")

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Incoming request: {request.method} {request.path} from {request.META.get('REMOTE_ADDR')}")
        response = self.get_response(request)
        logger.info(f"Response: {response.status_code}")
        return response
