# # Program to add two matrices using nested loop
#
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
#    print(r)




# X = [[2,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1,8],
#     [6,7,3,7],
#     [6,7,3,7],
#     [6,7,3,7],
#     [4,5,9,5]]
#
# result = [[0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0]]
#
# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#     for j in range(len(X[0])):
#         result[1 + i][1+j] = X[i][j] + Y[i][j]
#
# for r in result:
#    print(r)




# X =[['X', 'B', 'H', 'H', 'H'],  # 0   ♘  ✠  ⚔
#     ['H', 'H', 'H', 'B', 'H'],  # 1
#     ['H', 'H', 'H', 'H', 'H'],  # 2
#     ['H', 'H', 'B', 'H', 'H'],  # 3
#     ['H', 'H', 'H', 'H', 'H']  # 4
# ]  # 0,  1,  2,  3,  4
#
# Y =[['', '', '', '', ''],  # 0   ♘  ✠  ⚔
#     ['', '', '', '', ''],
#     ['', '', '', '', ''],
#     ['', '', '', '', ''],
#     ['', '', '',  '', '']]  # 0,  1,  2,  3,  4
#
# result = [['M','M','M','M','M','M','M',],
#         ['M','M','M','M','M','M','M',],
#         ['M','M','M','M','M','M','M',],
#         ['M','M','M','M','M','M','M',],
#         ['M','M','M','M','M','M','M',],
#         ['M','M','M','M','M','M','M',],
#         ['M','M','M','M','M','M','M',]]
#
# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#     for j in range(len(X[0])):
#         result[1 + i][1+j] = X[i][j] + Y[i][j]
#
# for r in result:
#    print(r)





# result_2 = []
# result_2 = [['M'] * 7]
# print(result_2)
# result_2 = result_2 * 7
# print(result_2)





# # Program to add two matrices using list comprehension
#
# X = [[12, 7, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# Y = [[5, 8, 1],
#      [6, 7, 3],
#      [4, 5, 9]]
#
# result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
#
# for r in result:
#     print(r)





# A = [[1, 4, 5, 12],
#     [-5, 8, 9, 0],
#     [-6, 7, 11, 19]]
#
# print("A =", A)
# print("A[1] =", A[1])      # 2nd row
# print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
# print("A[0][-1] =", A[0][-1])   # Last element of 1st Row
#
# column = [];        # empty list
# for row in A:
#   column.append(row[2])
#
# print("3rd column =", column)
# print(A)





matrix = [['M'] * 7 for i in range(7)]
# print(matrix)
# pprint.pprint(matrix)


# result = [[''] * 7 for i in range(7)]
# print(result)
# # pprint.pprint(matrix)


gmap = [
    ['X', 'B', 'H', 'H', 'H'],  # 0   ♘  ✠  ⚔
    ['H', 'H', 'H', 'B', 'H'],  # 1
    ['H', 'H', 'H', 'H', 'H'],  # 2
    ['H', 'H', 'B', 'H', 'H'],  # 3
    ['H', 'H', 'H', 'H', 'H']  # 4
]  # 0,  1,  2,  3,  4
# print(gmap)


import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])

matrix = np.array(matrix)
# result = np.array(result)
gmap = np.array(gmap)

# print(arr)
print(matrix)
print(gmap)
# print(result)


for i in range(len(gmap)):
    # iterate through columns
    for j in range(len(gmap[0])):
        matrix[1 + i][1 + j] = gmap[i][j] + matrix[i][j]

for r in matrix:
    print(r)






