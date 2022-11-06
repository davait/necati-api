#
# Flask environments configuration
#

class BaseConfig:
    APPLICATION_NAME = 'Necati REST API (Docker + Flask + MongoDB)'
    MONGODB_HOSTNAME = 'necati-mongo'
    MONGODB_PORT = '27017'
    MONGODB_USERNAME = 'necati'
    MONGODB_PASSWORD = 'necati'
    MONGODB_DATABASE = 'necati'
    API_HOST = '0.0.0.0'
    API_PORT = 9090
    API_DEBUG = True

class Development(BaseConfig):
    API_PORT = 9090
    API_DEBUG = True

class Testing(BaseConfig):
    API_PORT = 9090
    API_DEBUG = True

class Production(BaseConfig):
    API_PORT = 9090
    API_DEBUG = False
