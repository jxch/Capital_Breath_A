import tushare as ts

from . import dev_setting
from . import test_setting
from . import local_setting
from . import product_setting
from . import product_china_setting

config_dict = {
    'default': local_setting.LocalSetting,
    'dev': dev_setting.DevSetting,
    'test': test_setting.TestSetting,
    'local': local_setting.LocalSetting,
    'product': product_setting.ProductSetting,
    'product_china': product_china_setting.ProductChinaSetting
}

pro = ts.pro_api('34af7b2e7f3bbf2c48b0a12e0084c9099df78acd66f37ad5c92e0326')
