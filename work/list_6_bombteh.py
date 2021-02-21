
from os import system

robo_r = 2
robo_c = 2
option = ''
over = False


gmap = [
    ['H','B','H','H','H'],  # 0   ♘  ✠  ⚔
    ['H','H','H','B','H'],  # 1
    ['H','H','X','H','H'],  # 2
    ['H','H','B','H','B'],  # 3
    ['H','H','H','H','H']   # 4
]   # 0,  1,  2,  3,  4


# print(gmap[0])
# print(gmap[0][4])

# for (i, item) in enumerate(gmap, start=1):
#     print (i, item)

# for x in range(len(gmap)):
#     print (gmap[x])

# for i in range(len(gmap)):
#     for j in i:
#         print(j, end=" ")
#     print()

# print ("List index-value are : ")
# for i in range(len(gmap)):
#     print (i, end = " ")
#     print (gmap[i])



while option != 'x':

    ########## print the map #############
    system("cls")
    print()
    print("-" * 10)
    for r in range(len(gmap)):
        for c in range(len(gmap)):
            print(gmap[r][c], end=' ')
        print('|')
    print("-" * 10)
    print('\n\nCONTROLS: \na - left, \nd - right, \nx - exit, \nw - streeght, \ns - down' )
    ########## print the map #############




    ########## controls #############
    if over:
        print()
        print('GAME OVER')
        break

    option = input('>> ')

    if option == 'a':
        gmap[robo_r][robo_c] = 'H'
        robo_c -= 1
        if gmap[robo_r][robo_c] == 'B':
            over = True
            gmap[robo_r][robo_c] = 'D'
        else:
            gmap[robo_r][robo_c] = 'X'

    if option == 'd':
        gmap[robo_r][robo_c] = 'H'
        robo_c += 1
        if gmap[robo_r][robo_c] == 'B':
            over = True
            gmap[robo_r][robo_c] = 'D'
        else:
            gmap[robo_r][robo_c] = 'X'


    if option == 'w':
        gmap[robo_r][robo_c] = 'H'
        robo_r -= 1
        if gmap[robo_r][robo_c] == 'B':
            over = True
            gmap[robo_r][robo_c] = 'D'
        else:
            gmap[robo_r][robo_c] = 'X'

    if option == 's':
        gmap[robo_r][robo_c] = 'H'
        robo_r += 1
        if gmap[robo_r][robo_c] == 'B':
            over = True
            gmap[robo_r][robo_c] = 'D'
        else:
            gmap[robo_r][robo_c] = 'X'



    elif option == 'x':
        print('GAME OVER')
    ########## controls #############



# add movement left streeght
# add limits
# add mines + GAME OVER conditions