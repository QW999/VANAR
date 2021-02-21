
# module: order functionality


# HW2: complete this func

def process_option(food, option):
    # print(food.keys())
    food_name = list(food.keys())[option-1]
    food_price = food[food_name]

    print(food_price)
    print("You have chosen: ", option, food_name, "!", "  For unit price: ", food_price)

    # HW2: ask quantity
    # if ENTER = cancel

    # if ent numb = calc total (func separate func)
    # print total
    # ask confirmation (y/n)
    # ask for costumer name
    # save the order data in data/<name>order.txt

    q = int(input("How many? "))
    total = q * food_price
    print(food_name, "x", q, "=", total)


    # file = open("copy.txt", "w")
    # file.write("Your text goes here")
    # file.close()

    client_name = input("Your name pls: ")
    # file = open("data/" + client_name + ".txt", "w")
    # file.write(food_name + "|" + str(q) + str(food_price) + "|" + str(total))
    # file.close()

    with open("data/" + client_name + ".txt", "w") as file:
        file.write(food_name + "|" + str(q) + "|" + str(food_price) + "|" + str(total))



def confirmation():
    c = input("Press y/n for confirmation: ")
    if c == "y":
        print("Reservation confirmed!")
    elif c == "n":
        print("Reservation decline!")
    elif c == "":
        print("Cancel reservation")
    else:
        print("CK next time...")


def show_order_info():
    client_name = input("Your name in data: ")
    file = open("data/" + client_name + ".txt", "r")
    data = file.read()
    file.close()
    print(data)



