import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
my_key = "Key From OpenWeathermap"
account_sid = 'AC744d873862bcbab088d72535f19f5f85'
auth_token = 'Authentication Token From Twilio'

weather_params = {
    "lat": 39.065369,
    "lon": -108.569527,
    "appid": my_key,
    "cnt": 4
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today, rembember to bring an Umbrella.",
            from_='YOUR NUMBER FROM TWILIO',
            to='The "To" Number'
        )

    print(message.status)
