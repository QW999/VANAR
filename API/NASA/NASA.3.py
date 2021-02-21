import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)

Asteroids_Neo_Feed = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-02-14&end_date=2021-02-14&api_key=vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'

response = requests.get(Asteroids_Neo_Feed)
data = json.loads(response.text)
# pp.pprint(data)

# pp.pprint(data['near_earth_objects']['2021-02-14'])
for_date_list = data['near_earth_objects']['2021-02-14']
# print(type(for_date_list))
pp.pprint(for_date_list)

name_1_Asteroid = for_date_list[0]['name']
print('\nAsteroid nr.1 name: ', name_1_Asteroid)
print()
miss_distance_1_A_dict = for_date_list[0]
# print(type(miss_distance_1_A_dict))
print()
pp.pprint(miss_distance_1_A_dict)

distance_km = miss_distance_1_A_dict['close_approach_data']
pp.pprint(distance_km)
# print(type(distance_km))
print()

miss_distance_1_A_list_2 = distance_km[0]
pp.pprint(miss_distance_1_A_list_2)
# print(type(miss_distance_1_A_list_2))
print()

miss_distance_1_A_dict = miss_distance_1_A_list_2['miss_distance']['kilometers']
pp.pprint(miss_distance_1_A_dict)
print('\nDistance to', name_1_Asteroid, 'is', miss_distance_1_A_dict, 'km')




