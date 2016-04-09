from random import uniform
import math

class SenseHat(object):
    """
    Fake implementation of SenseHat to emulate behavior during development on a non Raspberry Pi
    environment.
    """

    LED = {} # Store the individual LED state.

    @staticmethod
    def _get_led_key(row, column):
        return 'row:'+str(row)+'c:'+str(column)

    def get_pixel(self, row, column):
        # Get the current or default
        key = self._get_led_key(row, column)
        return self.LED.get(key, [0, 0, 0])

    def set_pixel(self, row, column, color):
        key = self._get_led_key(row, column)
        self.LED[key] = color

    def clear(self):
        # Clear the LED dictionary
        self.LED.clear()

    @staticmethod
    def _sample():
        return uniform(10.3, 40.9)

    def get_humidity(self):
        return self._sample()

    def get_temperature(self):
        return self._sample()

    def get_pressure(self):
        return self._sample()

    def get_temperature_from_pressure(self):
        return self._sample()

    def get_temperature_from_humidity(self):
        return self._sample()

    @staticmethod
    def get_orientation_radians():
        return {'roll': 1.5708, 'pitch': 3.14159, 'yaw': 4.71239}

    def get_orientation_degrees(self):
        orientation = self.get_orientation_radians()
        for key, val in orientation.items():
            deg = math.degrees(val)  # Result is -180 to +180
            orientation[key] = deg + 360 if deg < 0 else deg
        return orientation

    @staticmethod
    def get_compass():
        return 4.71239
