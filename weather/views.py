import requests 
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appId= '08ce24b022ca7bd3edcdafc3a16d69ca'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appId

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()    
    

    cities = City.objects.all()


    allCities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        cityInfo = {
            'city': city.name,
            'temp': res["main"] ["temp"],
            'icon': res["weather"] [0] ["icon"]
        }

        allCities.append(cityInfo)

    context = {'allInfo': allCities, 'form': form}

    return render(request, 'weather/index.html', context)