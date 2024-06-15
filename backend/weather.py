import requests
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.debug(f"Response data: {data}")
        
        if data['cod'] == 200:
            weather_data = {
                'name': data['name'],
                'temp': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather_data
        else:
            logger.error(f"Error fetching weather data: {data['message']}")
            return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None

# Example usage:
api_key = 'a1f091c4f0238f190936f30d574ef4a6'
city = 'London'
weather = get_weather(city, api_key)
if weather:
    print(f"Weather in {weather['name']}: {weather['temp']}°C, {weather['description']}")
else:
    print("Failed to retrieve weather data.")
