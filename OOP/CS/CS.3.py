import pprint
pp = pprint.PrettyPrinter(indent=2)

class Employee:

    num_of_emps = 0
    raise_amount = 1.03

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return print(self.first, self.last, self.email)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp_1 = Employee('Adolf', 'Hitler', 100)
emp_2 = Employee('Iosiv', 'Stalin', 90)
# emp_3 = Employee(input('first: '), input('last: '), input('pay: '))

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# print(emp_3.raise_amount)

