
# ck if is ok   filter -> transform A-B  ->  transform B-A  -> ck
# def transformMoneyBack(dict): ..-> str



def fiterEmpties(input):
    output = input.strip()
    return output

def transformMoney(input):
    currency = input[-3:]
    value = float(input[:-3])
    output = {'value': value,
              'currency': currency}
    return output

data_1 = '100MDL'
data_1 = fiterEmpties(data_1)
res_1 = transformMoney(data_1)
print('1. ', data_1, '-->', res_1)

data_2 = '100MDL'
data_2 = fiterEmpties(data_2)
res_2 = transformMoney(data_2)
print('1. ', data_2, '-->', res_2)

data_3 = '100MDL'
data_3 = fiterEmpties(data_3)
res_3 = transformMoney(data_3)
print('1. ', data_3, '-->', res_3)
