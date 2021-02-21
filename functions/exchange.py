
def main():
    print_name(input('Hello who are you? '))
    usd_rate = float(input('USR rate: '))
    money = int(input('How much money do you have? '))
    operation = exchange(usd_rate, money)
    print(operation)

def print_name(name):
    print('HI', name)

def exchange(usd_rate, money):
    operation = round(money * usd_rate, 2)
    # return operation
    print('Echange USD to MDL', operation)


main()