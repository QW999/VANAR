
class FruitBox:

    def __init__(self, apples, oranges):
        self.apples = apples
        self.oranges = oranges

        if apples != int(apples) or oranges != int(oranges):
            print("Put just whole fruits!!")

        elif apples > 50 or oranges > 50:
            print("Full box!!")

        elif apples < 0 or oranges < 0:
            print("No negative!!")

    def __add__(self, other): # self + other/adunare
        return "Apples from: box1 + box2 = ", self.apples + other.apples, \
               "Oranges from: box1 + box2 = ", self.oranges + other.oranges


a_box = FruitBox(10, 20)

box1 = FruitBox(5, -10)
box2 = FruitBox(10, 20)
box3 = box1 + box2
print(box3)
