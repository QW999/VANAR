
# def buyTicket( touristName, seat, hour ):
#     ticket = {}
#     ticket[touristName] = input('Enter touristName: ')
#     ticket[seat] = input('Enter seat: ')
#     ticket[hour] = input('Enter hour: ')
#     return ticket
# print(buyTicket("touristName", "seat", "hour"))



print()
def buyTicket( touristName, seat, hour ):


    print('Places in bus:')
    for i in range(1, 11):
        i = str(i)
        a = i + "A"
        b = i + "B"
        c = i + "C"
        d = i + "D"
        print('Booking class: ', a, b, c, d)
        if b == seat or c == seat or d == seat or a == seat:
            print('Found your place. Pls register now!')
        # else:
        #     print('PLs buy tkt!')
        #     break    ..........??????????????
    print()


    ticket = {"touristName": touristName,
    "seat": seat,
    "hour": hour}


    print()
    if len(touristName) >= 5:
        print('touristName ok!')
    else:
        print('Pls enter correct name!')

    print()
    if hour == "11:00" or  hour == "11:30" or hour == "12:00":
        print('Bon voyage!')
    else:
        print('Sorry you can not enter!')


    print()
    return ticket
print()
print(buyTicket("Lora Abams", "4B", "11:00"))













