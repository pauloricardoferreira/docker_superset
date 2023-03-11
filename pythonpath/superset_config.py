# Superset specific config
ROW_LIMIT = 5000

SUPERSET_WEBSERVER_PORT = 8088

# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
# and encrypting sensitive information on the database
# Make sure you are changing this key for your deployment with a strong key.
# You can generate a strong key using `openssl rand -base64 42`

SECRET_KEY = 'supersersecret'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
#vSQLALCHEMY_DATABASE_URI = 'sqlite:////path/to/superset.db'
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset:superset@postgres-prd/superset"

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

BABEL_DEFAULT_LOCALE = "pt_BR"

BABEL_DEFAULT_FOLDER = "superset/translations"

LANGUAGES = {
    "pt_BR": {"flag": "br", "name": "Brazilian Portuguese"},
    "en": {"flag": "us", "name": "English"},
    "es": {"flag": "es", "name": "Spanish"},
    "pt": {"flag": "pt", "name": "Portuguese"},
}

#exemplo de onde fica o arquivo
APP_ICON = "/static/assets/custom_images/icon.svg"
FAVICONS = [{"href": "/static/assets/custom_images/icon.svg"}]
