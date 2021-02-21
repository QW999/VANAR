from os import system

# gmap[robo_r][robo_c] = center of square
robo_r = 2
robo_c = 2
option = ''
over = False

gmap = [
    ['H', 'B', 'H', 'H', 'H'],  # 0   ♘  ✠  ⚔
    ['H', 'H', 'H', 'B', 'H'],  # 1
    ['H', 'H', 'X', 'H', 'H'],  # 2
    ['H', 'H', 'B', 'H', 'H'],  # 3
    ['H', 'H', 'H', 'H', 'H']  # 4
]  # 0,  1,  2,  3,  4
# print(len(gmap[0]))

while option != 'x':
    try:
        ########## print the map #############
        system("cls")
        print()
        print("-" * 10)
        for r in range(len(gmap[0])):
            for c in range(len(gmap[0])):
                print(gmap[r][c], end=' ')
            print('|')
        print("-" * 10)
        print('\n\nCONTROLS: \na - left, \nd - right, \nx - exit, \nw - streeght, \ns - down')

        ########## controls #############
        if over:
            print()
            print('GAME OVER')
            break

        option = input('>> ')


        if option == 'a':
            gmap[robo_r][robo_c] = 'H'
            robo_c -= 1

        if option == 'd':
            gmap[robo_r][robo_c] = 'H'
            robo_c += 1

        if option == 'w':
            gmap[robo_r][robo_c] = 'H'
            robo_r -= 1

        if option == 's':
            gmap[robo_r][robo_c] = 'H'
            robo_r += 1

        if gmap[robo_r][robo_c] == 'B':
            over = True
            gmap[robo_r][robo_c] = 'D'

        if gmap[robo_r][robo_c] == 'M':
            over = True
            gmap[robo_r][robo_c] = 'D'

        else:
            gmap[robo_r][robo_c] = 'X'


        if option == 'x':
            over = True

    except IndexError:
        print('list assignment index out of range')
        print('GAME OVER')
        break