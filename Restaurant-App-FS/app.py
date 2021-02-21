
from menu import *
from order import *

option = -1
while option != 0:
    # if option == "":
    #     print("Cancel reservation!")
    #     break
    food = load_menu()
    # print(food)
    # print_menu(food)
    option = print_menu(food)
    # if option != 9:
    #     process_option(food, option)
    # else:
    #     show_order_info()

    if option == 9:
        show_order_info()
    else:
        process_option(food, option)
        confirmation()
