from . import base_setting


class LocalSetting(base_setting.BaseSetting):
    DEBUG = False
    SERVER_PORT = 8080
    APP_NAME = "Capital-Breath-A[local]"
    DB_CAPITAL = 'mysql+pymysql://root:jiang155.@aws.jiangxicheng.xyz:3306/capital'
