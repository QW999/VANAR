import numpy as np

A = np.arange(4)
print('A =', A)

B = np.arange(49).reshape(7, 7)
print('B =', B)

for i in B:
    i = str(i)
print(B)

# '''
# Output:
# A = [0 1 2 3]
# B = [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]





# import numpy as np
#
# A = np.array([[1, 1], [2, 1], [3, -3]])
# print(A.transpose())
#
# # '''
# # Output:
# # [[ 1  2  3]
# #  [ 1  1 -3]]
# # '''