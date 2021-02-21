from os import system
import numpy as np

robo_r = 1
robo_c = 1
option = ''
over = False

gmap = [['X', 'B', 'H', 'H', 'H'],  # 0   ♘  ✠  ⚔
    ['H', 'H', 'H', 'B', 'H'],  # 1
    ['H', 'H', 'H', 'H', 'H'],  # 2
    ['H', 'H', 'B', 'H', 'H'],  # 3
    ['H', 'H', 'H', 'H', 'H']] # 4]
matrix = [['M'] * (len(gmap) + 2) for i in range(len(gmap) + 2)]
matrix = np.array(matrix)

for i in range(len(gmap)):
    for j in range(len(gmap[0])):
        matrix[1 + i][1 + j] = gmap[i][j] + matrix[i][j]
for r in matrix:
    print(r)

while option != 'x':
        ########## print the map #############
        system("cls")
        print("-" * 15)
        for r in range(len(matrix[0])):
            for c in range(len(matrix[0])):
                print(matrix[r][c], end=' ')
            print('|')
        print("-" * 15)
        print('\n\nCONTROLS: \na - left, \nd - right, \nx - exit, \nw - streeght, \ns - down')
        ########## controls #############
        if over:
            print()
            print('GAME OVER')
            break
        print('ban on cross border: M')
        option = input('>> ')
        if option == 'a':
            matrix[robo_r][robo_c] = 'H'
            robo_c -= 1
        if option == 'd':
            matrix[robo_r][robo_c] = 'H'
            robo_c += 1
        if option == 'w':
            matrix[robo_r][robo_c] = 'H'
            robo_r -= 1
        if option == 's':
            matrix[robo_r][robo_c] = 'H'
            robo_r += 1
        if matrix[robo_r][robo_c] == 'B':
            over = True
            matrix[robo_r][robo_c] = 'D'
        if matrix[robo_r][robo_c] == 'M':
            over = True
            matrix[robo_r][robo_c] = 'D'
        else:
            matrix[robo_r][robo_c] = 'X'
        if option == 'x':
            over = True
