"""
Pi Panther application module.

Pi Panther composed of API modules and sample web API interfaces.
This module packages /api and / packages.
"""
from flask import Flask, render_template
from app.api.routes import api # API routes
from app.web.views import site # Web site views

# Application Version
__version__ = "0.1.0-alpha"

# Define Flask application
app = Flask(__name__)

# Add api prefix
app.register_blueprint(site, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

@app.errorhandler(404)
def page_not_found(exception):
    """
    Default 404 Handler.
    """
    return render_template("404.html", message=exception), 404
