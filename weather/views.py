import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7b11662c6a48426b789891bdf5a3d238'
    city = 'Delhi'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()


    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        # r1 = requests.get(url.format(city))
        # print(r1.text)

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    # print(weather_data)

    # print(city_weather)
    context = {'weather_data' : weather_data , 'form' : form}
    return render(request , 'weather/weather.html',context)
