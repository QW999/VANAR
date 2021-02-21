import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)

# import datetime
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))


from datetime import date
today = date.today()
print("Today's date:", today)
print(type(today))
today = str(today)
print(today)
print(type(today))


# Asteroids_Neo_Feed = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-02-14&end_date=2021-02-14&api_key=vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'
Asteroids_Neo_Feed = 'https://api.nasa.gov/neo/rest/v1/feed?start_date='+ today + '&end_date=' + today + '&api_key=vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'

# url_Asteroids = 'https://api.nasa.gov/neo/rest/v1/feed?'
# API_Asteroids = 'vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'


# # start_date = input('start_date=')
# start_date = 'start_date=2021-02-14'
# # end_date = input('end_date=')
# end_date = 'end_date=2021-02-14'

# Asteroids_Neo_Feed = 'https://api.nasa.gov/neo/rest/v1/feed?' + 'start_date' + '&' + 'end_date' + '&api_key=' + 'vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'



response_2 = requests.get(Asteroids_Neo_Feed)
data_2 = json.loads(response_2.text)
pp.pprint(data_2)