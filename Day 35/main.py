import requests

api_key = "87001bdd339a6ca72cffc3d54b76cd33"
my_parameters = {
    'lat': 33.158092,
    'lon': -117.350594,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=my_parameters)
weather_data = response.json()

weather_slice = weather_data['hourly'][:12]
will_rain = False

for hour in weather_slice:
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella')