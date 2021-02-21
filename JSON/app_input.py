
import json

file = open("data/person_input.json", "w")

name = input("Your name: ")
dob = int(input("Your dob: "))

person = {"name": name,
          "dob": dob}

# json.dump(person, file)
json.dump(person, file, indent=2)
print(person)

