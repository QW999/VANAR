# Age calculator

current_year = 2020
birth_year = int(input())
age = current_year - birth_year
print(age)



# def cube(num):
#     print("SLS")
#     return num*num*num
#
# result = cube(3)
# print(result)



# def max(a, b, c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
#
# print(max(11,2,3))



# password = 'arahide'
# Enter_password = ''
# pass_count = 0
# pass_limit = 3
# out_of_enter = False
#
# while Enter_password != password and not (out_of_enter):
#     if pass_count < pass_limit:
#         Enter_password = input('Enter pass: ')
#         pass_count += 1
#     else:
#         out_of_enter = True
#
# if out_of_enter:
#     print('If ou forgot pass ask for administrator!')
#
# else:
#     print('Correct pass!')



password = 'arahide'
Enter_password = ''
pass_limit = 0
out_of_enter = False

while Enter_password != password and not (out_of_enter):
    if pass_limit < 3:
        Enter_password = input('Enter pass: ')
        pass_limit += 1
    else:
        out_of_enter = True

if out_of_enter:
    print('If ou forgot pass ask for administrator!')

else:
    print('Correct pass!')



