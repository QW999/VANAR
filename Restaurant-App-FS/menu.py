
# module: menu functionality

import os


def load_menu():
    food_txt = open("data/food.txt", "r")
    data = food_txt.read()
    lines = data.split()

    # print(data)
    # print(lines)

    food = {}
    for line in lines:
        segments = line.split("|")
        # food = {segments[0]: segments[1]}
        food[segments[0]] = float(segments[1])
        # print("-->", segments)
    # print("-->", food)

    return food


# HW1: use os.system _cls

os.system("cls")
def print_menu(food):
    print("\n######  MENU  ######")
    print("9 Show order info")
    print("0 EXIT")
    n = 1
    for f in food:
        print(n, f)
        n += 1
    print("######  MENU  ######")

    option = int(input("chose >>> "))
    return option

