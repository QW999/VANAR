
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return print(self.first, self.last, self.email)


emp_1 = Employee('Adolf', 'Hitler', 100)
emp_2 = Employee('Iosiv', 'Stalin', 90)
# emp_3 = Employee(input('first: '), input('last: '), input('pay: '))

print(emp_1.email)
print(emp_2.email)
# print(emp_3.email)

print(emp_1.fullname())