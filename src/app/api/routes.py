"""
ReST API module.

This module handles ReST API endpoints.
"""
from random import randint
from flask import jsonify, request, url_for, redirect, abort
from app.api.decorators import crossdomain
from . import api

# Check if Sense HAT is available. If not use FAKE one. Helpful during development.
try:
    from sense_hat import SenseHat
except ImportError:
    from app.api.sense_hat_fake import SenseHat

sense = SenseHat()

def _get_pixel(row, column):
    """
    Helper function to get pixel value of given row and column.
    """
    color = sense.get_pixel(row, column)
    return {'row': row, \
            'column': column,\
            'color': color}

def _set_pixel(row, column, color):
    """
    Helper function to set color of given pixel row and column.
    """
    sense.set_pixel(row, column, color)

def _get_pixel_row(row):
    """
    Helper function to get array of given row's columns.
    """
    pixels = []
    for column in range(8):
        pixels.append(_get_pixel(row, column))
    return pixels

@api.route('/temperature', methods=['GET'])
@crossdomain('*')
def temperature():
    """
    API endpoint to get the temperature value.

    GET /temperature
    """
    celcius = sense.get_temperature()
    fahrenheit = (celcius*(9/5))+32
    celcius_from_humidity = sense.get_temperature_from_humidity()
    celcius_from_pressure = sense.get_temperature_from_pressure()
    return jsonify(celcius=celcius, \
        fahrenheit=fahrenheit, \
        celcius_from_pressure=celcius_from_pressure, \
        celcius_from_humidity=celcius_from_humidity)

@api.route('/humidity', methods=['GET'])
def humidity():
    """
    API endpoint to get the humidity value.

    GET /humidity
    """
    return jsonify(humidity=sense.get_humidity())

@api.route('/pressure', methods=['GET'])
def pressure():
    """
    API endpoint to get the pressure.

    GET /pressure
    """
    return jsonify(millibars=sense.get_pressure())

# Sense Hat Pixels
@api.route('/pixels', methods=['GET', 'DELETE'])
def pixel_grid():
    """
    API endpoint to get 8x8 pixel grid values and DELETE HTTP verb to reset the 8x8 pixel grid.

    GET /pixels
    DELETE /pixels

    TODO: API change: From DELETE to POST with json input data.
    """
    if request.method == 'DELETE':
        sense.clear()
    grid = []
    for row in range(8):
        grid = grid + _get_pixel_row(row)
    return jsonify(pixels=grid)

@api.route('/pixels/<int:row>', methods=['GET'])
def pixel_row(row):
    """
    API endpoint to get pixels by row.

    GET /pixels/<int:row>
    """
    if row > 7:
        abort(400) # Bad Request
    pixels = _get_pixel_row(row)
    return jsonify(pixels=pixels)

@api.route('/pixels/<int:row>/<int:column>', methods=['GET', 'POST'])
def pixel(row, column):
    """
    API endpoint to get single pixel value for given row and column. POST will set random pixel color.

    GET /pixels/<int:row>/<int:column>
    POST /pixels/<int:row>/<int:column>

    TODO: API change: POST to accept json data for color.
    """
    if row > 7 or column > 7:
        abort(400) # Bad Request
    if request.method == 'GET':
        return jsonify(_get_pixel(row, column))
    elif request.method == 'POST':
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        _set_pixel(row, column, color)
        return redirect(url_for('api.pixel', row=row, column=column))

@api.route('/orientation', methods=['GET'])
def orientation():
    """
    API endpoint to get orientation data in both radians and degrees.

    GET /orientation
    """
    radians = sense.get_orientation_radians()
    degrees = sense.get_orientation_degrees()
    return jsonify(radians=radians, degrees=degrees)

@api.route('/compass', methods=['GET'])
def compass():
    """
    API endpoint to get compass data.

    GET /compass
    """
    return jsonify(north=sense.get_compass())
