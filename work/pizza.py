# grade_1 = 8.9999999999
# grade_2 = 8.3333333
# grade_3 = 5.5555555
#
# print(round(grade_1 + grade_2 + grade_3 / 3, 2))
#
# nota_finala = grade_1 + grade_2 + grade_3 / 3
#
# print(f'Nota medie este {round(nota_finala, 3)}')





is_VIP_client = False

food_name = 'Pizza'
food_price = 50.00
food_quantity_disponibile = 99
food_quantity = int(input('Enter food quantity: '))

distance_to_client = int(input('Enter distance to client: '))

if food_quantity > 0 and food_quantity <= food_quantity_disponibile:
   print('Your order is in processing!')
else:
   print(f'Can not delivery {food_quantity} pizza')
   print(f'Disponibile: {food_quantity_disponibile} pizza')


cost_food = food_price * food_quantity
if cost_food > 0:
    print('Order accepted.')

cost_delivery_free = cost_food >= 200 and distance_to_client <= 20.00 \
                                      or is_VIP_client == True


print(food_name, ' x', food_quantity, ' =', cost_food)

print('Is delivery free? ', cost_delivery_free)





