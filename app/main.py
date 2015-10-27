from flask import Flask

from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    """Factory method for creating flask app.

    :param config_name: string
        name of config module for flask app.
    :return: flask app
    """
    app = Flask(__name__)
    app.config.from_object(config_name)
    bootstrap.init_app(app)
    db.init_app(app)

    from blueprints import blueprint
    app.register_blueprint(blueprint)

    return app


if __name__ == '__main__':
    app = create_app('config')
    app.run(debug=True)