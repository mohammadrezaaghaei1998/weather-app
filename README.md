# weather-app
weather-app



Description

This is a simple Django web application that provides weather information for multiple cities.
It allows users to search for the weather in a specific city and view the current weather as well as a 5-day forecast.

Features

Displays weather information for default cities (Berlin, Paris, London, New York, Tokyo).
Allows users to search for the weather in a custom city.
Shows the current weather and a 5-day forecast for the selected city.
Weather data is retrieved from the OpenWeatherMap API.


Usage

When you open the application, you'll see the current weather for default cities.
To search for the weather in a custom city, enter the city name in the input field and click the "Search" button.
The application will display the current weather and a 5-day forecast for the selected city.


Technologies Used
Python
Django
Requests (for making API calls)
HTML/CSS (using Bulma CSS framework)


API Key
To use this application, you need to obtain an API key from OpenWeatherMap. Once you have the API key, replace the api_key variable in the views.py file with your key:
api_key = 'YOUR_API_KEY_HERE'


License

This project is licensed under the MIT License.
