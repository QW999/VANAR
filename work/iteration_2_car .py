
# start = 1    # a) startimg conditions
# finish = 10  # b) finish conditions
#
# step = start
# while step <= finish:  # b) finish conditions
#     # code to repeat BEGIN
#     print('# ', end="")    # "\n"  _new line
#     # code to repeat END
#     step = step + 1   #c) how it iterates /  steps





# start = 1
# finish = 10
#
# a_stat_1 = 3
# a_stat_2 = 7
#
# car = 5
#
# step = start
# print("\n")
# while step <= finish:
#     print(step, end="")
#     print("---", end=" ")
#     step += 1
#
# print("\n\n")





# start = 1
# finish = 10
#
# a_stat_1 = 3
# a_stat_2 = 7
#
# car = 5
#
# step = start
# print("\n")
# while step < finish:
#     print(step, end="")
#     print("---", end=" ")
#     step += 1
#
# print(finish)
# print("\n\n")





# start = 1
# finish = 10
#
# a_stat_1 = 3
# a_stat_2 = 7
#
# car = 5
#
# step = start
# print("\n")
# while step <= finish:
#     print(step, end="")
#     if step != finish:
#         print("---", end=" ")
#     step += 1
#
# print("\n\n")





start = 1
finish = 10

a_stat_1 = 3
a_stat_2 = 7

car = int(input('Enter car location nr 1-10: '))
while True:
    if car <= 1 or car >= 10:
        print('Pls enter correct nr!')

    step = start
    print("\n")

    while step <= finish:
        print(step, end="")
        if step != finish:
            print("---", end=" ")
        step += 1

    step = start
    print("\n")
    while step <= finish:
        # if step == car and car >= 1 and car <= 10:
        #     print('H', end="")
        if step == a_stat_1 and step == car or step == a_stat_2 and step == car:
            print("HX", end="")
        elif step == a_stat_1 or step == a_stat_2:
            print("X", end="")
        else:
            print("0", end="")
        if step != finish:
            print("---", end=" ")
        step += 1

    print("\n\n")

    break