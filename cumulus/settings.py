from pyrax.cf_wrapper.client import CFClient

from django.conf import settings


CUMULUS = {
    "API_KEY": None,
    "AUTH_URL": "us_authurl",
    "AUTH_VERSION": "1.0",
    "AUTH_TENANT_NAME": None,
    "AUTH_TENANT_ID": None,
    "REGION": "DFW",
    "CNAMES": None,
    "CONTAINER": None,
    "CONTAINER_URI": None,
    "CONTAINER_SSL_URI": None,
    "SERVICENET": False,
    "TIMEOUT": 5,
    "TTL": CFClient.default_cdn_ttl,  # 86400s (24h), pyrax default
    "USE_SSL": False,
    "USERNAME": None,
    "STATIC_CONTAINER": None,
    "STATIC_CONTAINER_URI": None,
    "STATIC_CONTAINER_SSL_URI": None,
    "INCLUDE_LIST": [],
    "EXCLUDE_LIST": [],
    "HEADERS": {},
    "GZIP_CONTENT_TYPES": [],
    "USE_PYRAX": True,
    "PYRAX_IDENTITY_TYPE": None,
    "FILE_TTL": CFClient.default_cdn_ttl,
    'PUBLIC': True,
    'X_ACCOUNT_META_TEMP_URL_KEY': None,
    'X_STORAGE_URL': None,
    'X_TEMP_URL_TIMEOUT': 600,
    'X_TEMP_URL_BASE': 'https://storage101.dfw1.clouddrive.com'
}

if hasattr(settings, "CUMULUS"):
    CUMULUS.update(settings.CUMULUS)

# set the full rackspace auth_url
if CUMULUS["AUTH_URL"] == "us_authurl":
    CUMULUS["AUTH_URL"] = "https://auth.api.rackspacecloud.com/v1.0"
elif CUMULUS["AUTH_URL"] == "uk_authurl":
    CUMULUS["AUTH_URL"] = "https://lon.auth.api.rackspacecloud.com/v1.0"
