
# 'S' - loc gol
# 'T' - trandafir/ roses
# 'L' - lalea / tulips

garden = [
    #   0,   1,  2
    [ 'T', 'L', 'L' ],   # 0
    [ 'L', 'S', 'S' ],   # 1
    [ 'L', 'S', 'S']    # 2
]
print(garden[1])
print(garden[0][0])

for row in garden:
    for col in row:
        print( col, end=' ' )
    print()


roses = 0
tulips = 0
space = 0

for row in garden:
    for col in row:
        if col == 'T':
            roses += 1
            # print('roses: ', roses)
        if col == 'L':
            tulips += 1
            # print('tulips: ', tulips)
        if col == 'S':
            space += 1
            # print('space: ', space)

print()
print('roses: ', roses)
print('tulips: ', tulips)
print('space: ', space)
print()
print("CALCUL NR 1")
nr_tot_de_spatii = roses + tulips + space
# print(nr_tot_de_spatii)
roses_pr = roses * 100 / nr_tot_de_spatii
print('roses_pr: ', round(roses_pr, 2) , "%")
tulips_pr = tulips * 100 / nr_tot_de_spatii
print('tulips_pr: ', round(tulips_pr, 2), "%")
print()
print("CALCUL NR 2")
nr_tot_de_spatii_plantate = roses + tulips
roses_pr_pl = roses * 100 / nr_tot_de_spatii_plantate
print('roses_pr_pl', roses_pr_pl, "%")
tulips_pr_pl = tulips * 100 / nr_tot_de_spatii_plantate
print('tulips_pr_pl: ', tulips_pr_pl, "%")







