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

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employee(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developer('William', 'LaPorta', 50000, 'Java')
dev_2 = Developer('Marcus', 'Sugar', 60000, 'Python')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

mgr_1.add_employee(dev_2)

print(mgr_1.email)
mgr_1.print_employee()
print('-'*50)

mgr_1.remove_emp(dev_1)
mgr_1.print_employee()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))


# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
