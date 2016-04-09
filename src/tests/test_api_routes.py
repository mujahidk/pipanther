import unittest
from app import app

class APITestCase(unittest.TestCase):
    API_URI = '/api/'

    def setUp(self):
        # create a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def _get_uri(self, uri):
        return self.API_URI + uri

    def _get(self, uri):
        return self.app.get(self._get_uri(uri))

    def test_temperature(self):
        response = self._get('temperature')
        self.assertEqual(response.status_code, 200, "Successful GET should return 200 OK response.")
        cors_header = response.headers['Access-Control-Allow-Origin']
        self.assertEqual(cors_header, '*')
        self.assertEqual(response.content_type, "application/json")

    def test_humidity(self):
        result = self._get('humidity')
        self.assertEqual(result.status_code, 200)

    def test_pressure(self):
        result = self._get('pressure')
        self.assertEqual(result.status_code, 200)

    def test_pixels(self):
        result = self._get('pixels')
        self.assertEqual(result.status_code, 200)

    def test_pixels_row(self):
        result = self._get('pixels/8')
        self.assertEqual(result.status_code, 400)

    def test_pixels_row_column(self):
        result = self._get('pixels/1/2')
        self.assertEqual(result.status_code, 200)

        # Test POST method
        uri = self._get_uri('pixels/1/1')
        result = self.app.post(uri, data="some data", content_type='application/json')
        self.assertEqual(result.status_code, 302) #Redirect to GET

    def test_orientation(self):
        result = self._get('orientation')
        self.assertEqual(result.status_code, 200)

    def test_compass(self):
        result = self._get('compass')
        self.assertEqual(result.status_code, 200)
