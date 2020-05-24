from django.shortcuts import render
import requests


def Index(request):

    if request.POST:
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7f58fb81d202f06c8b815b95b72d4473'
        r = requests.get(url.format(city)).json()
        temp_in_cel = "{:.2f}".format((r['main']['temp'] - 32) * 5/9)

        city_weather = {
            'name': r['name'],
            'temp': temp_in_cel ,
            'humidity': r['main']['humidity'],
            'wind': r['wind']['speed'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        return render(request, 'weather/index.html', {'city_weather': city_weather})
    else:
        return render(request, 'weather/index.html')
