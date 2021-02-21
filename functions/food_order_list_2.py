
def calculateCost(quantity, price):
    totalCost1 = quantity * price
    return totalCost1


food_names = ['salat', 'pizza', 'soup']
food_price = [15.00, 75.00, 25.00]
food_q = [2, 1, 3]


order_cost = [calculateCost(a, b) for a, b in zip(food_price, food_q)]
print('order_cost: ',order_cost)


bill = {}
for name in food_names:
    for price in order_cost:
        bill[name] = price
print('The bill: ', bill)


totalCost = sum(order_cost)
print('The totalCost: ', totalCost)


