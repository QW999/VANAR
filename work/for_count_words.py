
# for n in range(10, 0, -1):
#     print(n)




# # Python code to demonstrate
# # how to remove numeric digits from string
# # using filter and lambda
#
# # initialising string
# ini_string = "akshat123garg"
#
# # printing initial ini_string
# print("initial string : ", ini_string)
#
# # using filter and lambda
# # to remove numeric digits from string
# res = "".join(filter(lambda x: not x.isdigit(), ini_string))
#
# # res = ini_string
# # printing result
# print("final string : ", str(res))




# # Python code to demonstrate
# # how to remove numeric digits from string
# # using join and isdigit
#
# # initialising string
# ini_string = "Geeks123for127geeks"
#
# # printing initial ini_string
# print("initial string : ", ini_string)
#
# # using join and isdigit
# # to remove numeric digits from string
# res = ''.join([i for i in ini_string if not i.isdigit()])
#
# # printing result
# print("final string : ", res)





# # Python code to demonstrate
# # how to remove numeric digits from string
# # using translate
# from string import digits
#
# # initialising string
# ini_string = "Geeks123for127geeks"
#
# # printing initial ini_string
# print("initial string : ", ini_string)
#
# # using translate and digits
# # to remove numeric digits from string
# remove_digits = str.maketrans('', '', digits)
# res = ini_string.translate(remove_digits)
#
# # printing result
# print("final string : ", res)




# print()
# sms = " HI! My phone nr is 069123456, call me pls! "
# for i in sms:
#     if not i.isdigit():
#         print(''.join([i]), end='')




# sms = " HI! My phone nr is 069123456, call me pls! "
# no_digits = []
# # Iterate through the string, adding non-numbers to the no_digits list
# for i in s:
#     if not i.isdigit():
#         no_digits.append(i)
#
# # Now join all elements of the list with '',
# # which puts all of the characters together.
# result = ''.join(no_digits)





# x = re.sub(r"\d+", "NUMB", str(x))




# print(''.join(filter(str.isdigit, sms)))




# print(''.join([i for i in sms if not i.isdigit()]))





# # Python program to Remove all
# # digits from a list of string
# import re
# def remove(list):
#     pattern = '[0-9]'
#     list = [re.sub(pattern, '', i) for i in list]
#     return list
# # Driver code
# list = ['4geeks', '3for', '4geeks']
# print(remove(list))




# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)



# sms = " HI! My phone nr is 069123456, call me pls! "
# for c in sms:
#     if c != '0' and c != '1' and c != '2' and c != '3' and c != '4' and c != '5' and c != '6' and c != '7' and c != '8' and c != '9':
#         print(c, end='')
#     else:
#         print('*', end='')





# sms = " HI! My phone nr is 069123456, call me pls! "
# for c in sms:
#     if c not in '0123456789':
#         print(c, end='')
#     else:
#         print('*', end='')
# print()





# sms = " HI! My phone nr is 069123456, call me pls! "
# for c in sms:
#     if c in '0123456789':
#         print('*', end='')
#     else:
#         print(c, end='')
# print()




# text = "HI! I like the for loop in Python. It took  me a minute to understand it!"
# count_words = 0
# for c in text:
#     if c == " ":
#         count_words += 1
# print("TEXT", c)
# print("Total words: ", count_words)
#
# sentence = 0
# for j in text:
#     if j == '!' or j == '.' or j == '?' or j == '...':
#         sentence += 1
# print('Sentences :', sentence)






count = int(input('how many grades?'))
for n in range(1, count + 1):
    grade = int(input('enter grade ' + str(n) + ': '))
    print(n)
print('after', n)