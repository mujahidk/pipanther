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

@site.route('/pixels')
def pixels():
    """
    Raspberry Pi pixels
    """
    return render_template("pixels.html")

@site.route('/temperature')
@site.route('/humidity')
def temperature():
    """
    Raspberry Pi temperature
    """
    return render_template("temperature.html")
