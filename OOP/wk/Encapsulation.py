
class car:

    def __init__(self, name, mileage):
        self._name = name                #protected variable
        self.mileage = mileage

    def description(self):
        return f"The {self._name} car gives the mileage of {self.mileage}km/l"
obj = car("BMW 7-series",39.53)

#accessing protected variable via class method
print(obj.description())

#accessing protected variable directly from outside
print(obj._name)
print(obj.mileage)