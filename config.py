class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:thegoblet2@localhost/factory_application'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True