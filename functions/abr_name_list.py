
people = ['John', 'Marry', 'Jerry', 'Jan', 'Eufrat']

def filterPeopleByJ(names):
    filtered = []
    for name in names:
        if name[0] == 'J':
            filtered.append(name)
    return filtered

selected_people = filterPeopleByJ(people)
print('selected_people: ', selected_people)

####################################################

people = ['John', 'Marry', 'Terry', 'Dan', 'Eufrat']

def generateInitial(names):
    transformed = []
    for name in names:
        transformed.append(name[0] + '.')
    return transformed

initials = generateInitial(people)

print('initials: ', initials)

#####################################################

namesN = ['John', 'Marry', 'Terry', 'Dan', 'Eufrat']
surnamesS = ['David', 'Moon', 'Huiery', 'Balan', 'Cufifrat']

def generateInitialdict(names, surnames):
    initials2dict = {}
    for name in names:
        for surname in surnames:
            initials2dict[name[0]] = surname[0]
    return initials2dict

initials = generateInitialdict(namesN, surnamesS)
print('initials: ', initials)

#####################################################

namesN2 = ['John', 'Marry', 'Terry', 'Dan', 'Eufrat']
surnamesS2 = ['David', 'Moon', 'Huiery', 'Balan', 'Cufifrat']

def generInitList2(namesN2, surnamesS2):
    initlist2 = []
    for a in namesN2:
        for b in surnamesS2:
            initlist2.append(a[0] + b[0])

    return initlist2

gil2 = generInitList2(namesN2, surnamesS2)
print('gil2: ', gil2)

#####################################################

# namesN2 = ['John', 'Marry', 'Terry', 'Dan', 'Eufrat']
# surnamesS2 = ['David', 'Moon', 'Huiery', 'Balan', 'Cufifrat']
#
# def generInitList2(namesN2, surnamesS2):
#     initlist21 = []
#     initlist22 = []
#     for a in namesN2:
#         initlist21.append(a[0])
#     print(initlist21)
#     for b in surnamesS2:
#         initlist22.append(b[0])
#     print(initlist22)
#
#     x = lambda a, b: a + b
#     print(x(a[0], b[0))
#
#     # for a in initlist21:
#     #     for b in initlist22:
#     #         c = a + b
#     #         print(c)
#
#
#     return initlist21, initlist22
#
# gil2 = generInitList2(namesN2, surnamesS2)
# print('gil2: ', gil2)


