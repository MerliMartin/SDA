"""
Implement a class to allow us to create different types of mammals
skin, birth-no kids, skin_type ( hair, fur)
class <name of class>
construct  - common
methods to implement what is unique
examples of the mammals
"""


class Mammals:
    def __init__(self, name, type, skin_type, birth_num):
        self.name = name
        self.type = type
        self.skin_type = skin_type
        self.birth_num = birth_num

    def __str__(self):
        return f"Mammal name is {self.name}. {self.name} is {self.type} and the skin type is {self.skin_type} " \
               f"and {self.name} gives birth to {self.birth_num} mammals!"


mammal_1 = Mammals("Tina", "whale", "hairy", 4)
print(mammal_1)
