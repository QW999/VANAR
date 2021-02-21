
class Audi:
  def description(self):
    print("This the description function of class AUDI.")

class BMW:
  def description(self):
    print("This the description function of class BMW.")
audi = Audi()
bmw = BMW()
for car in (audi,bmw):
 car.description()