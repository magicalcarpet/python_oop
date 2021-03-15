import datetime

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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




emp_1 = Employee('Tom', 'Cruise', 5_000_000)
emp_2 = Employee('Dwayne', 'Johnson', 6_000_000)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('-'*40)

my_date = datetime.date(2021, 7, 13)
print(Employee.is_workday(my_date))

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Stevie-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

