
from os import system
import numpy as np

robo_r = 1
robo_c = 1
option = ''
over = False

gmap = [
    ['X', 'B', 'H', 'H', 'H'],  # 0   ♘  ✠  ⚔
    ['H', 'H', 'H', 'B', 'H'],  # 1
    ['H', 'H', 'H', 'H', 'H'],  # 2
    ['H', 'H', 'B', 'H', 'H'],  # 3
    ['H', 'H', 'H', 'H', 'H']  # 4
]  # 0,  1,  2,  3,  4
# print(len(gmap[0]))


print()
s = len(gmap) + 2
print("Lenght r/c= ", s)
matrix = [['M'] * s for i in range(s)]
matrix = np.array(matrix)
gmap = np.array(gmap)

print(matrix)
print(gmap)

for i in range(len(gmap)):
    # iterate through columns
    for j in range(len(gmap[0])):
        matrix[1 + i][1 + j] = gmap[i][j] + matrix[i][j]

for r in matrix:
    print(r)

while option != 'x':
    try:

        ########## print the map #############
        system("cls")
        print()
        print("-" * 15)
        for r in range(len(matrix[0])):
            for c in range(len(matrix[0])):
                print(matrix[r][c], end=' ')
            print('|')
        print("-" * 15)
        print('\n\nCONTROLS: \na - left, \nd - right, \nx - exit, \nw - streeght, \ns - down')
        ########## print the map #############

        ########## controls #############

        # a = len(gmap[0])
        # print('ban on cross border:')
        # for row in range(0, a):
        #     for col in range(0, a):
        #         if (col == 0 or col == (a - 1) or ((row == 0 or row == (a - 1)) and (col > 0 and col < (a - 1)))):
        #             print("H", end=" ")
        #         else:
        #             print(" ", end=" ")
        #     print()

        if over:
            print()
            print('GAME OVER')
            break
        print('ban on cross border: M')

        option = input('>> ')

        if option == 'a':
            matrix[robo_r][robo_c] = 'H'
            robo_c -= 1
        # else:
        #     matrix[robo_r][robo_c] = 'X'

        if option == 'd':
            matrix[robo_r][robo_c] = 'H'
            robo_c += 1
        # else:
        #     matrix[robo_r][robo_c] = 'X'

        if option == 'w':
            matrix[robo_r][robo_c] = 'H'
            robo_r -= 1
        # else:
        #     matrix[robo_r][robo_c] = 'X'

        if option == 's':
            matrix[robo_r][robo_c] = 'H'
            robo_r += 1
        # else:
        #     matrix[robo_r][robo_c] = 'X'

        if matrix[robo_r][robo_c] == 'B':
            over = True
            matrix[robo_r][robo_c] = 'D'
        # else:
        #     matrix[robo_r][robo_c] = 'X'

        if matrix[robo_r][robo_c] == 'M':
            over = True
            matrix[robo_r][robo_c] = 'D'
        else:
            matrix[robo_r][robo_c] = 'X'

        if option == 'x':
            over = True
        ########## controls #############

    except IndexError:
        print('list assignment index out of range')
        print('GAME OVER')
        break

