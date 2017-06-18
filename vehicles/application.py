from flask import Flask
from flask_cors import CORS
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def generate_application(config=None):
    """Generate an application from a given configuration file."""
    application = Flask(__name__)
    application.config.from_object(config or 'vehicles.config.dev')
    CORS(application, send_wildcard=True)
    application.url_map.converters['regex'] = RegexConverter
    # application.register_blueprint(blueprint_file.generate_blueprint_callback(application.config))
    return application


def generate_test_application(config=None):
    """Generate a test application from a given configuration file."""
    application = Flask(__name__)
    application.config.from_object(config or 'vehicles.config.test')
    CORS(application, send_wildcard=True)
    return application
