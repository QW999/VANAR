# algorithms with simple and multi lists
# aggregation ? HW1




# cases = [ 50, 10, 100, 150, 0, 50, 50, 100, 100, 100]
# s = 0
# l = []
# for i in cases:
#     if i >= 0:
#         s = s + i
#         print(s)
#         l.append(s)
# print(l)




# products_cat_prices = [ 0.5, 10.00, 1.50, 5.50, 2.50 ]
# discount = 0.9
# for i in range(len(products_cat_prices)):
#     if products_cat_prices[i] >= 5:
#         products_cat_prices[i] = products_cat_prices[i] * discount
#
# for i in range(len(products_cat_prices)):
#     print(i,")", products_cat_prices[i])




# rating = [5, 3, 1, 4, 5, 2, 5]
# for i in range(len(rating)):
#     print("user", i + 1, "=", rating[i], end=" ")
#     for r in range(rating[i]):
#         print("*", end="")
#     print()




# calc statistica conform marcii
#indicator numeric pentru parcare
while True:
    p = [ None, None, "BMW", None, None, "Audi", "BMW"]
    print(p)
    user_car_brand = input("Enter car name: ")
    user_park_index = int(input("Place? "))
    if p[user_park_index] == None:
        print("Pls park your car!")
    else:
        print("Not free!")

    total = len(p)
    free = 0
    for i in range(len(p)):
        if p[i] == None:
            free += 1
    print("Parking(free/total): ", free, "/", total, " places.")
    p.insert(user_park_index, user_car_brand)
    print(p)

    for j in p:
        if j != None:
            print(j, end=" ")
            x = p.count(j)
            print(x)




# Hard worker
# ...schimb de pozitii

# people = ["J", "M", "F"]
# print("Before", people)
# temp = people[0]
# people[0] = people[1]
# people[1] = temp
# print("After", people)




# while True:
#
#     people = ["J", "M", "F"]
#
#     print("Before", people)
#
#     print(len(people))
#
#     b = int(input("Indexul actual a persoanei care necesita modificare : "))
#     a = int(input("Elibereaza persoana din indexul: "))
#
#     if a <= len(people) and b <= len(people):
#         print('Next')
#     else:
#         print('Enter correct nr!')
#
#         break
#
#     temp = people[a]
#     people[a] = people[b]
#     people[b] = temp
#
#     print("After", people)




# # Initialize array
# arr = [5, 2, 8, 7, 1];
# temp = 0;
#
# # Displaying elements of original array
# print("Elements of original array: ");
# for i in range(0, len(arr)):
#     print(arr[i], end=" ");
#
# # Sort the array in ascending order
# for i in range(0, len(arr)):
#     for j in range(i + 1, len(arr)):
#         if (arr[i] > arr[j]):
#             temp = arr[i];
#             arr[i] = arr[j];
#             arr[j] = temp;
#
# print();
#
# # Displaying elements of the array after sorting
#
# print("Elements of array sorted in ascending order: ");
# for i in range(0, len(arr)):
#     print(arr[i], end=" ");