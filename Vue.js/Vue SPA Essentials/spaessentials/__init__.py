import os
from flask import Flask, render_template
from flask_cors import CORS

print(__name__)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(
            app.instance_path,
            'spaessentials.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def home():
        # return os.getcwd()
        return render_template('index.html')

    # @app.route('/statuses', methods=['GET'])
    # def statuses():
    #     return 1

    from . import auth
    app.register_blueprint(auth.bp)

    from . import db
    db.init_app(app)

    from . import statuses
    app.register_blueprint(statuses.bp)
    app.add_url_rule('/', endpoint='index')

    return app
