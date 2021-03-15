class Employee:
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@action.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.number_of_employees)

emp_1 = Employee('Tom', 'Cruise', 5_000_000)
emp_2 = Employee('Dwayne', 'Johnson', 6_000_000)

print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_1.pay)

print("-"* 40)
print()

# The class variable 'raise_amount' is accessible from the class as well as
# from both instances because python first checks 
# 1. Whether the instance contains the attribute
# 2. Checks within the class 
# 3. Finally whether it is inheried 

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# By looking at the namespaces of the instance and 
# the class we can cleary see this

print(emp_1.__dict__)
print()
print(Employee.__dict__)

# We make changes to the class 

# Employee.raise_amount = 1.05

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Changes to the instance

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# emp_1 now has raise_amount within its namespace

print(emp_1.__dict__)

print(Employee.number_of_employees)
