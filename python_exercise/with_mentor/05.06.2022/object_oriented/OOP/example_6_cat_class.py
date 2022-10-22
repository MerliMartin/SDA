class Animal:
    def __init__(self, animal_name, num_of_legs):
        self.animal_name = animal_name
        self.num_of_legs = num_of_legs

    def say_name(self):
        print(f"My name is {self.animal_name}")

    def __str__(self):
        return f"{self.animal_name} is {self.num_of_legs} legs"


class Cat(Animal):
    def __init__(self, animal_name, num_of_legs, cat_name, age, sound):
        super(Cat, self).__init__(animal_name, num_of_legs)
        self.cat_name = cat_name
        self.age = age
        self.sound = sound

    def say_name(self):
        print(f"My name is {self.animal_name}")

    def __str__(self):
        return f"{self.cat_name} is {self.age} years old and says {self.sound}"


# class WildCat(Animal, Cat):
#     def __init__(self, animal_name, num_of_legs, cat_name, age, sound, habitat):
#         super(WildCat, self).__init__(animal_name, num_of_legs)
#         self.cat_name = cat_name
#         self.age = age
#         self.sound = sound
#         self.habitat = habitat
#
#     def say_name(self):
#         print(f"My name is {self.animal_name}")
#
#
# xx = WildCat("tiger", 4, "Mark", 7, "wraw", "jungle")
# print(xx.say_name())