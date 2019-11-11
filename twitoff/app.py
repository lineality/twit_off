"""
application logic for twifoff app
"""

from flask import Flask

def create_app():
    """Creat and configure an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Hello Twirld!'

    return app
