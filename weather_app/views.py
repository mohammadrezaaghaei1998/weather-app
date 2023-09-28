from django.shortcuts import render
import requests
import datetime
import random

        

def home(request):
    default_cities = ['Berlin', 'Paris', 'London', 'New York', 'Tokyo']

    api_key = '9f34e09c4c14625708681d3fc9c29860' #Your API_KEY (get your api of 'openweathermap.org')
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    forecast_url = 'https://api.openweathermap.org/data/2.5/forecast'

    weather_data = []

    for city in default_cities:
        parameters = {'q': city, 'appid': api_key, 'units': 'metric'}
        r = requests.get(url=current_weather_url, params=parameters)
        response = r.json()


        des = response['weather'][0]['description']
        icon = response['weather'][0]['icon']
        temp = response['main']['temp']
        day = datetime.date.today()

        city_data = {
            'city_name': city,
            'des': des,
            'icon': icon,
            'temp': temp,
            'day': day,
        }
        weather_data.append(city_data)

    user_city_data = None
    user_forecast_data = None

    if request.method == 'POST':
        if 'city' in request.POST:
            user_city = request.POST['city']

            parameters = {'q': user_city, 'appid': api_key, 'units': 'metric'}
            r = requests.get(url=current_weather_url, params=parameters)
            response = r.json()


            user_city_data = {
                'city_name': user_city,
                'des': des,
                'icon': icon,
                'temp': temp,
                'day': day,
            }

            forecast_parameters = {'q': user_city, 'appid': api_key, 'units': 'metric'}
            forecast_r = requests.get(url=forecast_url, params=forecast_parameters)
            forecast_response = forecast_r.json()
            
            forecast_data = forecast_response['list']
            user_forecast_data = []

            for forecast in forecast_data:
                date = forecast['dt_txt'].split()[0]
                time = forecast['dt_txt'].split()[1]
                temp = forecast['main']['temp']
                des = forecast['weather'][0]['description']
                icon = forecast['weather'][0]['icon']

                user_forecast_data.append({
                    'date': date,
                    'time': time,
                    'temp': temp,
                    'des': des,
                    'icon': icon,
                })

        else:
            user_city_data = None
            user_forecast_data = None

    return render(request, 'home.html', {'weather_data': weather_data, 'user_city_data': user_city_data, 'user_forecast_data': user_forecast_data})





