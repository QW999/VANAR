
# item = input()
# container = ["J", "M", "B"]
#
# for i in range(len(container)):
#     found = container[i] == item
#     print(">>>", i, container[i] == item)
#     if found:
#         break
#
# if found:
#     print(item, 'FOUND')
# else:
#     print(item, 'NOT FOUND')
#
# if container == item:
#     print('APP SUCCES')





# items = ["P", "M"]
# found = [False, False]
# container = ["J", "M", "B"]
#
# for j in range(len(items)):
#     for i in range(len(container)):
#         found = container[i] == items[j]
#         print(">>>", i, container[i] == items)
#         if found:
#             break
#
#     if found:
#         print(items[j], 'FOUND')
#     else:
#         print(items[j], 'NOT FOUND')





items = ["P", "M"]
found = [False, False]
container = ["J", "M", "B"]

for j in range(len(items)):
    for i in range(len(container)):
        found[j] = container[i] == items[j]
        # print(">>>", i, container[i] == items)
        if found[j]:
            break


for j in range(len(items)):
    if found[j]:
        print(items[j], 'FOUND')
    else:
        print(items[j], 'NOT FOUND')

