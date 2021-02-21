# dictionary = {}
# dictionary["new key"] = "some new entry" # add new dictionary entry
# dictionary["dictionary_within_a_dictionary"] = {} # this is required by python
# dictionary["dictionary_within_a_dictionary"]["sub_dict"] = {"other" : "dictionary"}
# print (dictionary)





# book = {
#     # key : value
#     'title': 'PYB',
#     'year' : 2020,
#     'author': 'JD'
# }
#
# print(book)
#
# if book['year'] >= 2000:
#     print('This book is fresh.')
# else:
#     print('This is a old book')





order = {
    'client' : 'JD',
    'item': 'Salat',
    'quantity': int(input('Enter quantity: ')),
    'price': 15.00
}

order['total'] = order['price'] * order['quantity']

if order['quantity'] >= 7:
    order_discounted = order['total'] - (order['total'] * 20 / 100)
    print('Price with discount: ', order_discounted)
else:
    order_discounted = order['total']


delivery_q = input('Do you need delivery? ')
if order['total'] >= 300:
    print('Free delivery')
    order["delivery"] = "free"
elif delivery_q == 'y':
    print('50$ in district area.')
    order['total'] = order['total'] + 50
elif delivery_q == 'n':
    print('CK in restaurant')
else:
    print('Pls answer!')


print('ORDER for: ', order['client'])
print('Food: ', order['item'])
print('Price * qty: ', order['price'], 'x', order['quantity'])
print('Total: ', order['total'])

print("")
print(order)





# Turning Keys Into Values and Vice Versa
#
# >>> a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# >>> new_dict = {}
# >>> for key, value in a_dict.items():
# ...     new_dict[value] = key
# ...
# >>> new_dict
# {1: 'one', 2: 'two', 3: 'thee', 4: 'four'}