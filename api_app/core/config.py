from starlette.config import Config
from _version import __version__

config = Config(".env")

# API settings
API_PREFIX = "/api"
PROJECT_NAME: str = config("PROJECT_NAME", default="Azure TRE API")
DEBUG: bool = config("DEBUG", cast=bool, default=False)
VERSION = __version__
API_DESCRIPTION = "Welcome to the Azure TRE API - for more information about templates and workspaces see the [Azure TRE documentation](https://github.com/microsoft/AzureTRE/blob/main/docs/concepts.md)"

# Resource Info
RESOURCE_LOCATION: str = config("RESOURCE_LOCATION", default="")
TRE_ID: str = config("TRE_ID", default="")
CORE_ADDRESS_SPACE: str = config("CORE_ADDRESS_SPACE", default="")
TRE_ADDRESS_SPACE: str = config("TRE_ADDRESS_SPACE", default="")

# State store configuration
STATE_STORE_ENDPOINT: str = config("STATE_STORE_ENDPOINT", default="")      # Cosmos DB endpoint
STATE_STORE_KEY: str = config("STATE_STORE_KEY", default="")                # Cosmos DB access key
COSMOSDB_ACCOUNT_NAME: str = config("COSMOSDB_ACCOUNT_NAME", default="")                # Cosmos DB account name
STATE_STORE_DATABASE = "AzureTRE"
STATE_STORE_RESOURCES_CONTAINER = "Resources"
STATE_STORE_RESOURCE_TEMPLATES_CONTAINER = "ResourceTemplates"
SUBSCRIPTION_ID: str = config("SUBSCRIPTION_ID", default="")
RESOURCE_GROUP_NAME: str = config("RESOURCE_GROUP_NAME", default="")


# Service bus configuration
SERVICE_BUS_FULLY_QUALIFIED_NAMESPACE: str = config("SERVICE_BUS_FULLY_QUALIFIED_NAMESPACE", default="")
SERVICE_BUS_RESOURCE_REQUEST_QUEUE: str = config("SERVICE_BUS_RESOURCE_REQUEST_QUEUE", default="")
SERVICE_BUS_DEPLOYMENT_STATUS_UPDATE_QUEUE: str = config("SERVICE_BUS_DEPLOYMENT_STATUS_UPDATE_QUEUE", default="")

# Managed identity configuration
MANAGED_IDENTITY_CLIENT_ID: str = config("MANAGED_IDENTITY_CLIENT_ID", default="")

# Logging and monitoring
APP_INSIGHTS_INSTRUMENTATION_KEY: str = config("APPINSIGHTS_INSTRUMENTATIONKEY", default="")

# Authentication
API_CLIENT_ID: str = config("API_CLIENT_ID", default="")
API_CLIENT_SECRET: str = config("API_CLIENT_SECRET", default="")
SWAGGER_UI_CLIENT_ID: str = config("SWAGGER_UI_CLIENT_ID", default="")
AAD_TENANT_ID: str = config("AAD_TENANT_ID", default="")

AAD_INSTANCE: str = config("AAD_INSTANCE", default="https://login.microsoftonline.com")
API_AUDIENCE: str = config("API_AUDIENCE", default=API_CLIENT_ID)
