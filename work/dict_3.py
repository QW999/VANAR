
# d = {
#     'a': 10,
#     'b': 100,
#     'c': 1000
# }



# product = {
#     'name': 'xPhone X',
#     'used': True,
#     'year': 2020,
#     'brand': 'Peach',
#     'price': {
#         'value': 1000.00,
#         'currency': 'EUR'
#         }
#     }
# print(product['name'])
# print(product['price']['value'], product['price']['currency'])





# # Declaring a dictionary
# d = {}
#
# # This is the list which we are
# # trying to use as a key to
# # the dictionary
# a = [1, 2, 3, 4, 5]
#
# # converting the list a to a string
# p = str(a)
# d[p] = 1
#
# # converting the list a to a tuple
# q = tuple(a)
# d[q] = 1
#
# for key, value in d.items():
#     print(key, ':', value)





from numerize import numerize

user = {
    'username': 'J007',
    'online': True,
    'email': 'J007@gmail.uk',
    'rating': int(input('Enter rating: ')),
    'friends': [
        'Marry888',
        'Candy001',
        'Peter99'
    ]
}

r = numerize.numerize(user['rating'])
if user["rating"] > 1:
    print('Our user has ', r, ' Likes')
elif user["rating"] == 1:
    print('Our user has ', r, ' Like')
elif user["rating"] == 0:
    print('Our user has no Like')
else:
    print('Pls enter correct value!')


while True:
    add_friend = str(input("Enter friend name: "))
    user["friends"].append(add_friend)
    print(type(add_friend))
    if add_friend == str:
        print('Name OK')
    # else:
    #     print('Pls enter correct name!')
    #     break


    print(user['username'])
    print(user['online'])
    print(user['email'])
    print(user['rating'])
    print(user['friends'][0][0])


    for i in range(len(user['friends'])):
        print('>>', user['friends'][i])