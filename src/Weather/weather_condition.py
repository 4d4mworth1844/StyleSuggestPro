'''
This module will return current weather condition based on 
conversation between Bot and user.
Then the current weather data will fetched into model to make recommender work more accurate
'''

import requests

def get_weather(api_key, city, country_code=''):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    # Construct the API endpoint URL
    endpoint = f'{base_url}?q={city},{country_code}&appid={api_key}'

    # Make the API request
    response = requests.get(endpoint)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        weather_data = response.json()
        
        # Extract relevant information from the API response
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        description = weather_data['weather'][0]['description']

        return f'The current temperature in {city} is {temperature}°C. Humidity: {humidity}%, Pressure: {pressure} hPa. Weather: {description}'
    else:
        return f'Error: Unable to retrieve weather data. Status Code: {response.status_code}'

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = ''
city = 'Da Nang'
country_code = "VN"

# Example: Get weather for New York, USA
weather_result = get_weather(api_key, city, country_code)
print(weather_result)
