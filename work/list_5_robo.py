
from os import system

print()
hp = 100
option = ''
over = False
robo_x = 4   # index 4
gmap = [' ','★','★',' ','♖',' ','⚔','⚔',' ',' ']


while option != 'x':
    print('Work from 1 til 8 index inclusiv!')
        ########## print the map #############
    system('cls')
    print()
    print("-" * 20)
    for i in range(len(gmap)):
        print(gmap[i], end=' ')
    print()
    print("-" * 20)
    for i in range(len(gmap)):
        print(i, end=' ')
    print('\n\nCONTROLS: a - left, d - right, x - exit', ' hp: ', hp,'%')
        ########## print the map #############


        ########## controls #############
    if gmap.index('♖') == 0:
        over = True
    if gmap.index('♖') == 9:
        over = True

    if hp == 0:
        gmap[robo_x] = ' '
        gmap[robo_x] = '☠'  # Mort ☠
        over = True

    if over:
        print('GAME OVER')
        break

    option = input('>> ')
    if option == 'a':
        gmap[robo_x] = ' '  # remove thr current position
        robo_x -= 1
        # print('left')
        if gmap[robo_x] == '⚔':  # Dinamit
            hp -= 50
            # gmap[robo_x] = '♖'
            # print('moved to index:', gmap.index('♖'))
            # print('hp: ', hp)
            # if hp == 0:
            #     gmap[robo_x] = '☠'  # Mort
            #     over = True
        if gmap[robo_x] == '★':  # healph
            hp += 50
            gmap[robo_x] = '♖'
            print('moved to index:', gmap.index('♖'))
        else:
            gmap[robo_x] = '♖'   # place it on this position
            print('moved to index:', gmap.index('♖'))


    elif option == 'd':
        gmap[robo_x] = ' '
        robo_x += 1
        # print('right')
        if gmap[robo_x] == '⚔':
            hp -= 50
            # gmap[robo_x] = '♖'
            # print('moved to index:', gmap.index('♖'))
            # if hp == 0:
            #     gmap[robo_x] = '☠'
            #     over = True
        if gmap[robo_x] == '★':
            hp += 50
            gmap[robo_x] = '♖'
            print('moved to index:', gmap.index('♖'))
        else:
            gmap[robo_x] = '♖'
            print('moved to index:', gmap.index('♖'))


    elif option == 'x':
        print('GAME OVER')
    print()
    print('Fin current loop')
    print()
    print()
        ########## controls #############




#   moove right/left   if 9 can not move right, limits
#   add var hp(healph points) = 100 each time Danger = -10....-100 = GAME OVER

