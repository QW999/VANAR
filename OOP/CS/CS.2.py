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


print('\nnum_of_emps: ', Employee.num_of_emps)

emp_1 = Employee('Adolf', 'Hitler', 100)
emp_2 = Employee('Iosiv', 'Stalin', 90)
# emp_3 = Employee(input('first: '), input('last: '), input('pay: '))

# print(emp_1.email)
# print(emp_2.email)
# # print(emp_3.email)

# print(emp_1.fullname())
emp_1.raise_amount = 1.05

print('emp_1 before raise: ', emp_1.pay, '  emp_2 before raise: ', emp_2.pay)
emp_1.apply_raise()
print('emp_1 after raise: ', emp_1.pay, '  emp_2 after raise: ', emp_2.pay)

# pp.pprint(emp_1.__dict__)
# pp.pprint(Employee.__dict__)

print('\nnum_of_emps: ', Employee.num_of_emps)