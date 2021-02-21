
file = open("data.txt", "r")
data = file.read()
# print(data)
# print(type(data))


# # parse data | METHOD 1:
# name = data[:6]
# price = float(data[6:12])
# q = int (data[-1:])
# total = q * price
# print(name, price, 'quantity: ', q, 'total: ', total)


# # parse data | METHOD 2:
segments = data.split()
print(segments)
name_0 = segments[0][0]
name = segments[0]
price = float(segments[1])
q = int(segments[2])
total = q * price
print(name_0, name, price, q, total)