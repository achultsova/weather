import requests 
from django.shortcuts import render
from .models import City

def index(request):
    appId= '08ce24b022ca7bd3edcdafc3a16d69ca'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appId

    
    

    cities = City.objects.all()


    allCities = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        cityInfo = {
            'city': city.name,
            'temp': res["main"] ["temp"],
            'icon': res["weather"] [0] ["icon"]
        }

        allCities.append(cityInfo)

    context = {'allInfo': cityInfo}

    return render(request, 'weather/index.html', context)