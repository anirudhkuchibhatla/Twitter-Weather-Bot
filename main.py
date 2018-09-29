import tweepy
import json
import requests
import keys
import time

consumer_key = keys.your_consumer_key
consumer_secret = keys.your_consumer_secret
access_token = keys.your_access_token
access_token_secret = keys.your_access_token_secret

API_key = keys.your_API_key


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

city = yourCity


response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID='+ API_key + '&units=imperial')
web_map = json.loads(response.text)


for i in range(3):
    temperature = (web_map['main']['temp'])
    message = 'The weather right now is ' + str(temperature) + '°F in Frisco, TX ' + "(" + str(i) + ')'
    message += " #DailyFriscoWeather"

    api.update_status(message)
    time.sleep(60)
