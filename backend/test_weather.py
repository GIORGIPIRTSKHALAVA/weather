import unittest
from unittest.mock import patch
from weather import get_weather

class TestWeather(unittest.TestCase):
    @patch('weather.requests.get')
    def test_get_weather_success(self, mock_get):
        mock_response = unittest.mock.Mock()
        expected_data = {
            'cod': 200,
            'name': 'London',
            'main': {'temp': 15.0, 'humidity': 80},
            'weather': [{'description': 'clear sky'}],
            'wind': {'speed': 1.5}
        }
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = unittest.mock.Mock()
        mock_get.return_value = mock_response

        api_key = 'fake_api_key'
        city = 'London'
        result = get_weather(city, api_key)
        expected_result = {
            'name': 'London',
            'temp': 15.0,
            'description': 'clear sky',
            'humidity': 80,
            'wind_speed': 1.5
        }
        self.assertEqual(result, expected_result)

    @patch('weather.requests.get')
    def test_get_weather_failure(self, mock_get):
        mock_response = unittest.mock.Mock()
        expected_data = {'cod': '404', 'message': 'city not found'}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status.side_effect = requests.HTTPError()
        mock_get.return_value = mock_response

        api_key = 'fake_api_key'
        city = 'InvalidCity'
        result = get_weather(city, api_key)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
