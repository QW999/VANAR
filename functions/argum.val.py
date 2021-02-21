
# string = "3.141"
# print(string)
# print(type(string))
#
# # converting string to float
# Float = float(string)
# print(Float)
# print(type(Float))


def inputInt(message_i):
    print('message_i', type(message_i))
    int_mes = int(message_i)
    print('int_mes: ', int_mes)
    print('int_mes', type(int_mes))
    return int_mes
inputInt(input('Enter inputInt message: '))

n = inputInt(input("Enter the first integer: "))
m = inputInt(input("Enter the second integer: "))

print( n + m )



def inputFloat(message_f):
    print('message_f', type(message_f))
    float_mes = float(message_f)
    print('float_mes: ', float_mes)
    print('float_mes', type(float_mes))
    return float_mes
inputFloat(input('Enter inputFloat message: '))




def inputBoolean(message_b):
    print('message_b', type(message_b))
    bool_mes = bool(message_b)
    print('bool_mes: ', bool_mes)
    print('bool_mes', type(bool_mes))
    return bool_mes
inputBoolean(input('Enter inputBoolean message: '))





def input_val(type_m, mess):
    if type_m == 'i':
        mess = int(mess)
    if type_m == 'f':
        mess = float(mess)
    if type_m == 'b':
        mess = bool(mess)

    return (print(mess, end=" "), print(type(mess)))

input_val(input('Type value: '), input('Enter mess: '))





def input_val(type_m, mess):
    while True:
        if type_m == 'i':
            mess = int(mess)
        if type_m == 'f':
            mess = float(mess)
        if type_m == 'b':
            mess = bool(mess)
        else:
            print('Incorect value!')
            break

        return (print(mess, end=" "), print(type(mess)))

input_val(input('Type value: '), input('Enter mess: '))