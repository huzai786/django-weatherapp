from django.shortcuts import render
from .forms import CityForm
from .models import City
import requests
from django.contrib import messages

def home(request):
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=c8a6a6ab8d86b9c283d304da65a11dc7'        

    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            city_count = City.objects.filter(name=city_name).count()
            if city_count == 0:
                form.save()
            elif city_count > 0:
                messages.error(request, 'A City with that name already exists!')

    form = CityForm()

                
    weather_data = []

    for city in cities:
        res = requests.get(url.format(city))
        r = res.json()
        if res.status_code == 200:
            city_weather = {
            'name': city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
        else:
            messages.error(request, 'No City exist with that name!')
    
    context={'form': form, 'weather_data': weather_data}
    return render(request, 'vocab/home.html', context)