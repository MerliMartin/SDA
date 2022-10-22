"""
We want to simulate a typical student in school
You have a student who can get a scholarship
this student is a person, so we should have a person class and the student inherits from this class
Then we have a possibility of a student also working.
so we have another class for employee. Employee inherits from the person class
lastly create the working student class that has a multiple inheritance
from both the employee and student class.
think of different methods you create inside each class since you are once
    *a student / currently a student
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old!"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hour):
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hour = num_of_hour

    def show_finance(self):
        return self.rate * self.num_of_hour


class Student(Person):
    def __init__(self, student_name, age, scholarship):
        Person.__init__(self, student_name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):  # multiple inheritance
    def __init__(self, name, age, rate, num_of_hour, scholarship, student_loan):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)
        self.student_loan = student_loan

    def show_finance(self):
        return self.rate * self.num_of_hour + self.scholarship

    def __str__(self):
        return f"{self.name} is {self.age} years old and earns {self.show_finance()} " \
               f"with a student loan of {self.student_loan}."


os1 = Person("John", 54)
os2 = Employee("Jack", 36, 20, 160)
os3 = Student("Agatha", 22, 1000)
os4 = WorkingStudent("Monica", 24, 9.5, 70, 550, 400)
print(os2.show_finance())
print(os3.show_finance())

print(os2)
