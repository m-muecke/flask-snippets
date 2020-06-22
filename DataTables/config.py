class Config:
    """Common configurations"""
    SECRET_KEY = 'SECRET_KEY'

class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
