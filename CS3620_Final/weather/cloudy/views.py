from django.shortcuts import render
from .models import City
import requests
from .forms import CityForm

def index(request):
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b31f140d6c681a4254ec4e45cfe1fe7c'
    
    form = CityForm()
    
    cities = City.objects.all()
    
    weather_data = []
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    # For each city in cities
    for city in cities:
        print(city)
        # connect to api and get city weather data
        city_weather = requests.get(url.format(city)).json()

        # map the weather data to city, temp, desc, and icon
        weather = {
            'city' : city_weather['name'],
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        # append that cities weather data to weather_data 
        weather_data.append(weather) 


    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'cloudy/index.html', context)

