from .base import *
DEBUG = os.getenv('DEBUG', False) == 'True'

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_ROOT = BASE_DIR / 'media'