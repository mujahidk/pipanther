"""
This module handles sample API consumer web pages.
"""
from flask import render_template
from . import site

@site.route('/')
def index():
    """
    Default page.
    """
    return render_template("index.html", message="Welcome to Pi Panther")
