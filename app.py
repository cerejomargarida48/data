from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_migrate import Migrate

from extensions import db, ma
from routes.data import register_routes


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://tonnie:tonnie@127.0.0.1:5432/data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def setup(app):
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)
    register_routes(app)
    docs = FlaskApiSpec(app)
    docs.register_existing_resources()


def main_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup(app)

    return app


if __name__ == '__main__':
    main_app().run(debug=False, port=5000)
