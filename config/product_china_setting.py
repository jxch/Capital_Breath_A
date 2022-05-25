from . import product_setting


class ProductChinaSetting(product_setting.ProductSetting):
    SERVER_HOST = "c.jiangxicheng.xyz"
    DB_CAPITAL = 'mysql+pymysql://root:jiang155.@aws.jiangxicheng.xyz:3306/capital'
