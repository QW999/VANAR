
# File: dict_popitem.py

# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
#
# while True:
#     try:
#         print(f'Dictionary length: {len(a_dict)}')
#         item = a_dict.popitem()
#         # Do something with item here...
#         print(f'{item} removed')
#     except KeyError:
#         print('The dictionary has no item now...')
#         break




d = {}
while True:
    key = input("Enter the key: ")
    val = input("Enter the value: ")
    d[key] = val
    for key, val in d.items():
        if key == "" or val == "":
            print("Stop loop")
            break
    else:
        print(d)
    # d.update({key: val})




# for i in range(3):
#     key = input('Enter the key: ')
#     val = input('Enter the value: ')
#     d[key] = val
#
# print('You hane now', len(d), 'values')
# print('The dictionary now contains', d)





# new_dict = {'Jan':31, 'Feb':29, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':30}
# a = iter(new_dict.items())
# default = object()
#
# while a:
#     elem = next(a, default)
#     # This check is to know whether iterator is exhausted or not.
#     if elem is default:
#         break
#     print("{} {}".format(*elem))





