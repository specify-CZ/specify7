import os
import json
from . import specify_settings as specify_defaults

DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_PORT = os.environ.get('DATABASE_PORT', '')

ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', 'password')
MASTER_NAME = os.getenv('MASTER_NAME', 'root')
MASTER_PASSWORD = os.getenv('MASTER_PASSWORD', ROOT_PASSWORD)
MIGRATOR_NAME = os.getenv('MIGRATOR_NAME', MASTER_NAME)
MIGRATOR_PASSWORD = os.getenv('MIGRATOR_PASSWORD', MASTER_PASSWORD)
APP_USER_NAME = os.getenv('APP_USER_NAME', MIGRATOR_NAME)
APP_USER_PASSWORD = os.getenv('APP_USER_PASSWORD', MIGRATOR_PASSWORD)

DEPOSITORY_DIR = '/volumes/static-files/depository'

REPORT_RUNNER_HOST = os.getenv('REPORT_RUNNER_HOST', '')
REPORT_RUNNER_PORT = os.getenv('REPORT_RUNNER_PORT', '')

WEB_ATTACHMENT_URL = os.getenv('ASSET_SERVER_URL', None)
WEB_ATTACHMENT_KEY = os.getenv('ASSET_SERVER_KEY', None)
WEB_ATTACHMENT_COLLECTION = os.getenv('ASSET_SERVER_COLLECTION', None)
SEPARATE_WEB_ATTACHMENT_FOLDERS = os.getenv('SEPARATE_WEB_ATTACHMENT_FOLDERS', None)

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_DB_INDEX = os.getenv('REDIS_DB_INDEX', 0)
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', None)
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', None)
CELERY_TASK_DEFAULT_QUEUE = os.getenv('CELERY_TASK_QUEUE', DATABASE_NAME)

ANONYMOUS_USER = os.getenv('ANONYMOUS_USER', None)
SPECIFY_CONFIG_DIR = os.environ.get('SPECIFY_CONFIG_DIR', '/opt/Specify/config')
TIME_ZONE = os.environ.get('TIME_ZONE', 'America/Chicago')
ALLOW_SUPPORT_LOGIN = os.environ.get('ALLOW_SUPPORT_LOGIN', False)
SUPPORT_LOGIN_TTL = int(os.environ.get('SUPPORT_LOGIN_TTL', 180))

# Resolve ALLOWED_HOSTS in the following precedence:
# - Use the ALLOWED_HOSTS environment variable (if present)
# - Otherwise, fallback to the default specified in settings/specify_settings.py
# - If still not defined, use the hard-coded default ['*']
# See https://github.com/specify/specify7/pull/6831
_env_allowed_hosts = os.getenv('ALLOWED_HOSTS', None)
_default_allowed_hosts = getattr(specify_defaults, 'ALLOWED_HOSTS', ['*'])
ALLOWED_HOSTS = (
    _default_allowed_hosts
    if _env_allowed_hosts is None
    else [host.strip() for host in _env_allowed_hosts.split(',')]
)

# Resolve CSRF_TRUSTED_ORIGINS in the following precedence:
# - Use the CSRF_TRUSTED_ORIGINS environment variable (if present)
# - Otherwise, fallback to the default specified in settings/specify_settings.py
# - If still not defined, use the hard-coded default ['https://*', 'http://*']
# See https://github.com/specify/specify7/pull/6831
_env_trusted_origins = os.getenv('CSRF_TRUSTED_ORIGINS', None)
_default_trusted_origins = getattr(
    specify_defaults, 'CSRF_TRUSTED_ORIGINS', ['https://*', 'http://*']
)
CSRF_TRUSTED_ORIGINS = (
    _default_trusted_origins
    if _env_trusted_origins is None
    else [origin.strip() for origin in _env_trusted_origins.split(',')]
)

# OAUTH_LOGIN_PROVIDERS configuration
# Supports two methods:
# 1. Environment variable: OAUTH_LOGIN_PROVIDERS with a JSON string
#    Example: '{"google": {"title": "Google", "client_id": "...", "client_secret": "...", "config": "https://accounts.google.com", "scope": "openid email"}}'
# 2. Direct Python configuration below (used if env var is not set)
_env_oauth_providers = os.getenv('OAUTH_LOGIN_PROVIDERS', None)
if _env_oauth_providers:
    # Parse from JSON environment variable
    try:
        OAUTH_LOGIN_PROVIDERS = json.loads(_env_oauth_providers)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in OAUTH_LOGIN_PROVIDERS environment variable: {e}")
else:
    # Default configuration - edit this or set OAUTH_LOGIN_PROVIDERS env var
    OAUTH_LOGIN_PROVIDERS = {
        # # Example: Google OAuth provider
        # 'google': {
        #     'title': "Google",
        #     'client_id': "your-google-client-id.apps.googleusercontent.com",
        #     'client_secret': "your-google-client-secret",
        #     'config': "https://accounts.google.com",
        #     'scope': "openid email",
        # },
        #
        # # Example: Custom OIDC provider
        # 'custom': {
        #     'title': "My Organization",
        #     'client_id': "your-client-id",
        #     'client_secret': "your-client-secret",
        #     'config': "https://auth.your-organization.com",
        #     'scope': "openid profile email",
        # },
    }