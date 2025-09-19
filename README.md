# Command-Line Weather App

A command-line tool, built with Python, that fetches and displays real-time weather data for any city in the world. This project demonstrates proficiency in working with third-party APIs, handling JSON data, and creating a user-friendly interface.

## Features

- Fetches live weather data from the OpenWeatherMap API.
- Displays key information: Condition, Temperature, Humidity, and Wind Speed.
- Includes a dynamic emoji that changes based on the weather and time of day (day/night).
- User-friendly loop allows checking multiple cities without restarting the script.
- Robust error handling for invalid city names or API issues.

## Setup & Usage

1.  **Get an API Key:**
    - Sign up for a free account at [OpenWeatherMap.org](https://openweathermap.org) to get an API key.

2.  **Install Dependencies:**
    - This script requires the `requests` library. Install it using pip:
      ```
      pip install requests
      ```

3.  **Run the Script:**
    - Download or clone the `weather.py` file.
    - Open the file and replace the placeholder `"YOUR_SECRET_API_KEY_GOES_HERE"` with your actual API key.
    - Run the script from your terminal:
      ```
      python weather.py
      ```
    - When prompted, enter a city name.

## Technologies Used

- Python 3
- `requests` Library
- OpenWeatherMap API
