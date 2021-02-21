import requests
import json

result = requests.get('http://data.fixer.io/api/latest?access_key=a57d57b3d314584d92fde35e74d2ff4c')

data = json.loads(result.text)

class Money:

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency
        rate = data['rates']['MDL']
        # if self.currency != "EUR":
        if self.currency == "MDL":
            self.value = round(self.value / rate, 2)
            self.currency = "EUR"
    print('MDL rate: ', data['rates']['MDL'])


    def __str__(self):  # convert to str
        # return "nothing"
        return "[" + str(self.value) + self.currency + "]"

    def __sub__(self, other):  # self - other/ scadere/ diferenta
        return Money(self.value - other.value,
                     self.currency)

    def __add__(self, other): # self + other/adunare
        return Money(self.value + other.value,
                     self.currency)


jun_salary = Money(1000, "MDL")
travel_cost = Money(700, "EUR")
rest = jun_salary - travel_cost  # self - other
add_sal_travel_cost = jun_salary + travel_cost  # self + other

print("jun_salary: ", jun_salary)
print("travel_cost: ", travel_cost)
print("rest: ", rest)
print("add_sal_travel_cost: ", add_sal_travel_cost)