from flask import Flask
from flask_apscheduler import APScheduler
import py_eureka_client.eureka_client as eureka_client
import os, traceback, threading, logging
from config import config_dict


class Config(object):
    SCHEDULER_API_ENABLED = True


logging.basicConfig(level=logging.INFO)
scheduler = APScheduler()
app = Flask(__name__)

env = os.getenv('CAPITAL_BREATH_A_ENV')
app.config.from_object(config_dict[env])
# app.config.from_object(config_dict['dev'])
app.logger.info("当前环境: " + env)


@app.route('/')
def hello_world():
    return 'Capital Breath A Service [started]'


@scheduler.task('cron', id='stock_daily', day='*', hour='10', minute='0', second='0')
def daily_job():
    app.logger.info('daily job [started]')


if env != 'product_china':
    eureka_client.init(eureka_server=app.config.get('EUREKA_SERVER'),
                       app_name=app.config.get('APP_NAME'),
                       instance_host=app.config.get('SERVER_HOST'),
                       instance_port=app.config.get('SERVER_PORT'),
                       ha_strategy=eureka_client.HA_STRATEGY_RANDOM)

if __name__ == '__main__':
    app.config.from_object(Config())
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=app.config.get('DEBUG'),
            threaded=app.config.get('THREADED'),
            port=app.config.get('SERVER_PORT'),
            host=app.config.get('HOST'))
