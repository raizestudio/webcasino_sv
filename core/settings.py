from pathlib import Path

import environ

env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
ALLOWED_HOSTS = ["*"]

# API
API_VERSION = env("API_VERSION", default="0.0.1")

# Application definition
INSTALLED_APPS = [
    "daphne",  # Must be first
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_celery_results",
    "django_filters",
    "channels",
    "corsheaders",
    "knox",
    "core",
    "auth_core",
    "users",
    "geo",
    "chat",
    "games",
    "financial",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "auth_core.middleware.LoggingMiddleware",
]

# Urls
ROOT_URLCONF = "core.urls"

# TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI_APPLICATION = "core.wsgi.application"


# Database
DATABASES = {
    "default": env.db(),
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "webcasino",
    #     "USER": "webcasino",
    #     "PASSWORD": "webcasino",
    #     "HOST": "localhost",
    #     "PORT": "5432",
    # }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ASGI
ASGI_APPLICATION = "core.asgi.application"

# Static files
MEDIA_DIR = BASE_DIR / "media"
if not MEDIA_DIR.exists():
    MEDIA_DIR.mkdir()

STATIC_URL = "static/"
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# User model
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"


# CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}

# REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("knox.auth.TokenAuthentication",),
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
    ],
}

# Authentication
AUTHENTICATION_BACKENDS = [
    "auth_core.backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Cache
CACHE_HOST = env("CACHE_HOST", default="")
CACHE_PORT = env("CACHE_PORT", default="6379")
CACHE_DB = env("CACHE_DB", default="")
CACHE_TTL = env("CACHE_TTL", default=60)
# CACHE_PASSWORD = env("CACHE_PASSWORD", default="")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{CACHE_HOST}:{CACHE_PORT}",
    }
}

# Celery
# CELERY_BROKER_URL = f"redis://{CACHE_HOST}:{CACHE_PORT}"
CELERY_BROKER_URL = "pyamqp://admin:admin@localhost:5672//"
CELERY_RESULT_BACKEND = "django-db"
# CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_RESULT_EXPIRES = 3600
CELERY_TASK_ACKS_LATE = True
CELERY_TASK_TRACK_STARTED = True

# Logging
LOG_DIR = BASE_DIR / "logs"
if not LOG_DIR.exists():
    LOG_DIR.mkdir()

# Knox
KNOX_TOKEN_MODEL = "knox.AuthToken"
REST_KNOX = {
    # "SECURE_HASH_ALGORITHM": "hashlib.sha512",
    # "AUTH_TOKEN_CHARACTER_LENGTH": 64,
    # "TOKEN_TTL": timedelta(hours=10),
    # "USER_SERIALIZER": "knox.serializers.UserSerializer",
    # "TOKEN_LIMIT_PER_USER": None,
    # "AUTO_REFRESH": False,
    # "AUTO_REFRESH_MAX_TTL": None,
    # "MIN_REFRESH_INTERVAL": 60,
    # "AUTH_HEADER_PREFIX": "Token",
    # "EXPIRY_DATETIME_FORMAT": api_settings.DATETIME_FORMAT,
    # "TOKEN_MODEL": "knox.AuthToken",
}

# IP Info
IP_INFO_URL = env("IP_INFO_URL")
IP_INFO_TOKEN = env("IP_INFO_TOKEN")

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} {name} - {message}",
            "style": "{",
        },
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "app.log",
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
        },
        "auth_core": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
