

# str JSON --> structure --> python

# json.load()  # reads from file
# json.loads()  # reads from str


import json

file = open("data/person.json", "r")
person = json.load(file)

print("name: ", person['name'])
print("dob: ", person['dob'])


# print(person)
# print(type(person))


