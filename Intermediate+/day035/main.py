import requests
import os

API_KEY=os.environ.get("OWM_API_KEY")
MY_LAT=12.971599
MY_LONG=77.594566

WEATHER_URL_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"

parameters={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4
}


response=requests.get(url=WEATHER_URL_ENDPOINT,params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data=response.json()
print(weather_data)

forecast_list=weather_data["list"]
print(forecast_list)

will_rain=False

for forecast in forecast_list:
    print(forecast["weather"][0]["id"])
    weather_codes=forecast["weather"][0]["id"]
    weather_codes=int(weather_codes)
    # rain_list=[forecast for forecast in forecast_list if weather_codes<800 ]
    if weather_codes < 700:
        will_rain=True
if will_rain:
    print("Bring an umbrella")




