import os

from celery import Celery

# Set default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Create Celery instance
celery_app = Celery("core")

# Load config from Django settings, using the CELERY namespace
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks from installed apps
celery_app.autodiscover_tasks()
