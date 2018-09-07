import requests
from django.shortcuts import render


def index(request):
    url = ' http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=56a41a7c5bdb682bb11ed12dc50bcce2'
    city = 'Odessa'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    print(city_weather)
    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)
