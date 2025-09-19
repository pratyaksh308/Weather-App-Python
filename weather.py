import requests
import json
from datetime import datetime
from config import API_KEY

def get_weather_emoji(weather_data):
    """Selects an emoji based on the weather condition and time of day."""
    condition = weather_data['weather'][0]['main'].lower()
    
    current_time = datetime.fromtimestamp(weather_data['dt'])
    sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'])
    sunset = datetime.fromtimestamp(weather_data['sys']['sunset'])
    is_night = not (sunrise < current_time < sunset)

    if "clear" in condition and is_night:
        return "🌃"
    elif "cloud" in condition:
        return "☁️"
    elif "rain" in condition or "drizzle" in condition:
        return "🌧️"
    elif "thunderstorm" in condition:
        return "⛈️"
    elif "snow" in condition:
        return "❄️"
    elif "clear" in condition:
        return "☀️"
    elif "haze" in condition or "mist" in condition or "fog" in condition:
        return "🌫️"
    else:
        return "🌍"

def main():
    api_key = API_KEY
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    while True:
        city = input("\nWhich city's weather would you like to check? ")

        if city.lower() == 'exit':
            break

        # Define query parameters for the API request.
        params = { 'q': city, 'appid': api_key, 'units': 'metric' }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            
            city_name = weather_data['name']
            country = weather_data['sys']['country']
            
            emoji = get_weather_emoji(weather_data)
            
            condition = weather_data['weather'][0]['main']
            temp = round(weather_data['main']['temp'])
            feels_like = round(weather_data['main']['feels_like'])
            humidity = weather_data['main']['humidity']
            wind_speed_kmh = round(weather_data['wind']['speed'] * 3.6)
            
            print("\n----------------------------------------")
            print(f"WEATHER IN {city_name.upper()}, {country}")
            print("----------------------------------------")
            print(f"  🔍  Condition:    {emoji} {condition}")
            print(f"  🌡️  Temperature:  {temp}°C (Feels like {feels_like}°C)")
            print(f"  💧  Humidity:     {humidity}%")
            print(f"  💨  Wind Speed:   {wind_speed_kmh} km/h")
            print("----------------------------------------")

        else:
            print(f"\nError fetching data: HTTP {response.status_code}")
            print("Please check the city name and that your API key is active.")

        another_city = input("\nCheck another city? (y/n): ")
        if another_city.lower() != 'y':
            break

    print("\nThanks for using the Weather App!")


if __name__ == "__main__":
    main()
