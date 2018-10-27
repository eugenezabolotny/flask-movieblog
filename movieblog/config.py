import os


class Config:
    MODE = 'Config'
    DEBUG = False


class DevConfig(Config):
    MODE = 'DevConfig'
    DEBUG = True


class TestConfig(Config):
    MODE = 'TestConfig'
    DEBUG = False


def run_config():
    env = os.environ.get('ENV')
    if env == 'DEV':
        return DevConfig
    if env == 'TEST':
        return TestConfig
    else:
        return Config
