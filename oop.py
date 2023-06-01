# Python object oriented programs

'''
A class is a blue print to create instances
'''

'''Instance variables contain data unique to each instance'''

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return'{}, {}'.format(self.first, self.last)


emp_1 = Employee('Abbey', 'Noyes', 900000)
emp_2 = Employee('Test', 'User', 20000)


print(emp_1.email)
print(emp_1.fullname())