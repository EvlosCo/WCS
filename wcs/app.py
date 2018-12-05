import os
from flask import Flask
from wcs.database import db


def create_app():
    flask_app = Flask()

    # Configure app
    flask_app.config['SQLALCHEMY_TRACT_MODIFICATIONS'] = False
    flask_app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://'
    f'{os.environ["DB_USER"]}:'
    f'{os.environ["DB_PASSWORD"]}@'
    f'{os.environ["DB_HOST"]}:'
    f'{os.environ["DB_PORT"]}/'
    f'{os.environ["DB_NAME"]}'

    db.init_app(flask_app)

    return flask_app
