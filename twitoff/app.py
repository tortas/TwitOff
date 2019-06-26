from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)

    # Tells app where to point in site
    @app.route("/")
    def root():
        return "Welcome to Twitoff!"

    return app