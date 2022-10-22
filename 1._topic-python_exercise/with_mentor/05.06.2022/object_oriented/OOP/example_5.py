class Employee:
    rise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@facebook.com'

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_rise(self):
        self.pay = int(self.pay * self.rise_amount)


ayo = Employee("Ayo", "Martin", 50000)
print(ayo.pay)
mary = Employee("Mary", "Ronaldo", 600000)
print(mary.pay)
ayo.pay = 33000
print(ayo.pay)
print(ayo.apply_rise())