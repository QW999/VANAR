
# def withdrawATM():
#     return 1000
#
# money = withdrawATM()
#
# price = 50
#
# rest = money - price
# print("We have ", rest, " money left")




# def calculateTax(amount):
#     TAX_RATIO = 20
#     tax = amount * TAX_RATIO / 100
#     return tax
#
# while True:
#     money = float(input('Enter amount: '))
#     tax = calculateTax(money)
#     rest = money - tax
#     print('Tax: ', tax, '%  from', money, 'rest is: ', rest)





import numpy as np


def calculateTax(amount):
    TAX_RATIO = 20
    tax = amount * TAX_RATIO / 100
    return tax

money = [1000.00,
         20.00,
         10000000.00]

tax = np.arange(3)
print(tax)

for i in range(3):
    tax[i] = calculateTax(money[i])

for i in range(3):
    print(money[i], ' => ', tax[i])