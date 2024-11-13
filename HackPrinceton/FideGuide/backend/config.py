import os

class Config:
    # Store general configuration settings for the app
    
    # OpenAI API Key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-api-key")

    # Yahoo Finance API Key (if necessary)
    YAHOO_FINANCE_API_KEY = os.getenv("YAHOO_FINANCE_API_KEY", "your-default-api-key")

    # Other app configurations
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
    DEBUG = os.getenv("FLASK_DEBUG", True)

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False

class TestingConfig(Config):
    """Testing environment configuration"""
    TESTING = True
    DEBUG = True
