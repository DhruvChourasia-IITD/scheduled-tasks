import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
phone_no = os.environ.get("PHONE_NO")

client = Client(account_sid, auth_token)
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast/"
parameters = {
    'appid' : api_key,
    'lat' : 28.55, #Latitude of IIT-Delhi
    'lon' : 77.19, #Longitude of IIT-Delhi
    'cnt' : 4
}

will_rain = False
data = requests.get(url=OWM_Endpoint, params=parameters)
data.raise_for_status()
for block in data.json()['list']:
    if block['weather'][0]['id'] <700:
        will_rain = True
if will_rain:
    message = client.messages.create(
        body='Bring an umbrella',
        from_='+16092860312',
        to=phone_no
    )
