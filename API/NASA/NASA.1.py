import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)

NASA_APIs = 'https://api.nasa.gov/planetary/apod?api_key=eHv7Q0ZedKx7JwWVhYooeev0RAoLshLAWyUuKbm4'
# APIs_key = 'eHv7Q0ZedKx7JwWVhYooeev0RAoLshLAWyUuKbm4'
# NASA_url = 'https://api.nasa.gov/planetary/apod?api_key='

response = requests.get(NASA_APIs)
data = json.loads(response.text)
# pp.pprint(data)

print(data['title'])
print('current_date: ', data['date'])
print('url: ', data['url'])

