import requests
import json
# import pprint

# pp = pprint.PrettyPrinter(indent=2, compact=True, width=30)

API_key = '7f99ceba5e37786e7dc8ee352ac36366'
# city_name = 'Chisinau'
city_name = input('Enter city_name: ')

# result = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
#                       + city_name + '&appid=' + API_key)
result = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
                      + city_name + '&appid=' + API_key + '&units=metric')
# print(result.text)
# print(type(result.text))

data = json.loads(result.text)
print(data)
# pp.pprint(data)
# print(type(data))

cod = data['cod']
print('\n\ncod', cod)

while True:
    if cod != 200:
        print('Err')
        break
    else:
        city_name = data['name']
        country = data['sys']['country']
        print('\n\ncountry:', country, '  city_name:', city_name)

        temp = data['main']['temp']
        print("temperature: ", temp)

        weather_in_city = data['weather'][0]['description']
        print(weather_in_city)
        break
