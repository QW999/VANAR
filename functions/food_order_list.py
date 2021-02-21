
import numpy as np
import math


def calculateCost(quantity, price):
    totalCost1 = quantity * price
    return totalCost1

r = calculateCost(1, 5)
print(r)



food_names = ['salat', 'pizza', 'soup']
food_price = [15.00, 75.00, 25.00]
food_q = [2, 1, 3]
order_cost = np.arange(3)
# order_cost = [0.0, 0.0, 0.0]
print(order_cost)





## calculate order cost

print(np.add(food_price, order_cost))
print(np.multiply(food_price, food_q))

order_cost = [food_price[i]*food_q[i] for i in range(len(food_price))]
print(order_cost)

order_cost = [a * b for a, b in zip(food_price, food_q)]
print('order_cost: ',order_cost)

order_cost = [calculateCost(a, b) for a, b in zip(food_price, food_q)]
print('order_cost: ',order_cost)

variable = math.prod(order_cost) # inmultire in list___ math
print(variable)
variable = math.prod(order_cost, start = 2)
print(variable)




## for print the bill

bill = {}
for name in food_names:
    for price in order_cost:
        bill[name] = price
print('The bill: ', bill, " ")




## return totalCost

totalCost = 0
for n in order_cost:
    totalCost += n
print('The totalCost: ', totalCost)

totalCost = sum(order_cost)
average_price = totalCost/len(order_cost)
print('The totalCost: ', totalCost)
print('average_pricet: ', average_price)




