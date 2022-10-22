class Employee:

    rise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_rise(self):
        self.pay = int(self.pay * self.rise_amount)


employee_1 = Employee("Sara", "Murk", 5100)  # creating first pobject etc. first employee in company
print(employee_1.fullname())  # checking employee fullname
employee_1.apply_rise()  # giving employee a 4% rise, it's the default percent.
print(employee_1.pay)  # checking employee new salary
print("==========================")
employee_2 = Employee("Terry", "Wild", 7500)
print(employee_2.fullname())  # checking another employee fullname
employee_2.rise_amount = 1.1  # it is changing the rise amount for only employee 2 , it is 10%
employee_2.apply_rise()  # it is applying the rise
print(employee_2.pay)  # checking the new salary
print("==========================")
Employee.rise_amount = 1.2  # applying new rise for all the new employees, its now 20%
print(Employee.rise_amount)  # checking the new rise amount
