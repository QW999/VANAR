
def greater(a, b):
    if a > b:
        return a
    return b

# def greatest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

def the_greatest(a, b, c):
    bigger = greater(a, b)
    return greater(bigger, c)

print(the_greatest(1,8,3))



