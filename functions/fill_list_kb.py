
def filListFromKb():
    values = []
    while True:
        v = input('Enter value: ')
        if v == '':
            break
        values.append(v)
    return values

values = filListFromKb()
print(values)