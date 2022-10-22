class Car:
    acceleration = 10

    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.in_motion = False
        self.speed = 0

    def drive(self):
        self.in_motion = True

    def accelerate(self):
        if self.in_motion:
            self.speed += self.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0


# Just tried to get the logic of the code, and what is the logic order for implementing code
my_old_bmw = Car("001TMR")
print(my_old_bmw)  # <__main__.Car objects at 0x0000021A63982DA0>
print(my_old_bmw.in_motion)  # False
print(my_old_bmw.speed)  # 0
print(my_old_bmw.registration_number)  # 001TMR
print("===================================================")
my_old_bmw.accelerate()
print(my_old_bmw.in_motion)  # False
print(my_old_bmw.speed)  # 0 - because I used if condition
print("===================================================")
my_old_bmw.drive()
print(my_old_bmw.in_motion)  # True
print(my_old_bmw.speed)  # 0
print("===================================================")
my_old_bmw.accelerate()
print(my_old_bmw.in_motion)  # True
print(my_old_bmw.speed)  # 10
print("===================================================")
my_old_bmw.stop()
print(my_old_bmw.speed)  # 0
print(my_old_bmw.in_motion)  # False

