
peole = ['John', 'Marry', 'Jack']


def filterePeopleBy_J(names):
    filtered = []
    for name in names:
        if name[0] == 'J':
            filtered.append(name)

        return filtered

selected_people = filterePeopleBy_J(peole)

print(selected_people)