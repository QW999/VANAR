
# Central European Bank

import requests
import json
import pprint


API_key = 'a57d57b3d314584d92fde35e74d2ff4c'
url = 'http://data.fixer.io/api/latest?access_key='
result = requests.get(url + API_key)
pp = pprint.PrettyPrinter(indent=4)

data = json.loads(result.text)
print('status_code is less than 400: ', result.ok)
print('result.status_code: ', result.status_code)
# print(result)
# pp.pprint(data)

current_date = data['date']
print('\ncurrent_date: ', current_date)
eur = data['base']
print('Central European Bank rate:', eur)
rates_in = data['rates']['MDL']
print('Changed in MDL: ', rates_in)
print('Pls insert local val:')
your_rate = data['rates'][input().upper()]
print(your_rate)


e = int(input('EUR _q: '))
v = your_rate
xx = e * v
xx = round(xx, 2)
print('Money in local val: ', xx)


