import requests 
from django.shortcuts import render

def index(request):
    appId= '08ce24b022ca7bd3edcdafc3a16d69ca'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appId

    city = 'London'
    res = requests.get(url.format(city)).json()
    
    cityInfo = {
        'city': city,
        'temp': res["main"] ["temp"],
        'icon': res["weather"] [0] ["icon"]
    }

    context = {'info': cityInfo}

    return render(request, 'weather/index.html', context)