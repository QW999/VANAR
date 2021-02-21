import requests
import json
import pprint

result = requests.get('http://data.fixer.io/api/latest?access_key=a57d57b3d314584d92fde35e74d2ff4c')
pp = pprint.PrettyPrinter(indent=2)

data = json.loads(result.text)
print('status_code is less than 400: ', result.ok)
print('result.status_code: ', result.status_code)
# pp.pprint(data)

print('\ncurrent_date: ', data['date'])
print('Central European Bank rate:', data['base'])
print('Changed in MDL: ', data['rates']['MDL'])
print('Pls insert local val', end=": ")
your_rate = data['rates'][input().upper()]
print('Rate of exchange is: ', your_rate)

q = int(input('EUR _q: '))
print('Money in local val: ', (round((q * your_rate), 2)))


