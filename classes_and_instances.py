# class Employee:
#         pass

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# a long and mistake prone way

# emp_1.first = 'Tom'
# emp_1.last = 'Cruise'
# emp_1.email = 'tom.cruise@action.com'
# emp_1.pay = 50000

# emp_2.first = 'dwayne'
# emp_2.last = 'johnson'
# emp_2.email = 'dwaynejohnson@action.com'
# emp_2.pay = 70000

# print(emp_1.email)
# print(emp_2.email)


# a more efficient way

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@action.com'

    def fullname(self):
        return '{0} {1}'.format(self.first, self.last)

emp_1 = Employee('Tom', 'Cruise', 5_000_000)
emp_2 = Employee('Dwayne', 'Johnson', 6_000_000)


print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

# INEFFICIENT WAY: Display full name

print('{0} {1}'.format(emp_1.first, emp_1.last))

# A more efficient way is to create a method in a class

print(emp_2.fullname())
print(Employee.fullname(emp_2))

