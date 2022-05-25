from . import base_setting


class LocalSetting(base_setting.BaseSetting):
    DEBUG = False
    SERVER_PORT = 8080
    APP_NAME = "Capital-Breath-A[local]"
