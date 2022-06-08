import requests


from twilio.rest import Client

api_key = "d87e1ef7e8f897c20440be376514eb11"

lat = 25.133699
long = 82.564430

parameter = {"lat": lat, 'lon': long, "appid": api_key, "units": "metric", "exclude": "current,daily,minutely"}

request = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
request.raise_for_status()
hourly = request.json()["hourly"]
last_12_hour = hourly[0:12]

account_sid = "AC1f12b0cd9b007018724f83cc068a7bb3"
auth_token = "abb5f74cdffcb1f60779949f97d0bb8d"
client = Client(account_sid, auth_token)

will_rain = False
for hour_data in last_12_hour:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain today remember to bring umbrella."
                                ,
        from_='+12248084396',
        to='+916390615878'
    )
    print(message.sid)

