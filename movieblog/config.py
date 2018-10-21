import os


class Config:
    TEST_VARIABLE = 'Config'


class DevConfig(Config):
    TEST_VARIABLE = 'DevConfig'


class TestConfig(Config):
    TEST_VARIABLE = 'TestConfig'


def run_config():
    env = os.environ.get('ENV')
    if env == 'DEV':
        return DevConfig
    if env == 'TEST':
        return TestConfig
    else:
        return Config
