from sqlalchemy import create_engine
import app
from flask import current_app


def engine_capital():
    with app.app.app_context():
        return create_engine(current_app.config.get('DB_CAPITAL'), encoding='utf8', pool_timeout=1000)
