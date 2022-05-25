from . import base_setting


class DevSetting(base_setting.BaseSetting):
    DEBUG = True
    SERVER_PORT = 8080
    APP_NAME = "Capital-Breath-A[dev]"
