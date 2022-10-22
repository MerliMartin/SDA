class Mammals:
    def __init__(self, name, habitat, birth_num, age):
        self.name = name
        self.habitat = habitat
        self.birth_num = birth_num
        self._age = age

    # setter
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age cannot be negative")

    # getter
    def get_age(self):
        return self._age

    def __str__(self):
        return f"{self.name}, {self.habitat}, {self._age}"


# whale = Mammals("Whale", "water", 1, 3)
# print(whale)
# whale.set_age(5)
# print(whale.get_age())
# print(whale)
#
# whale.set_age(-1)

# Inheritance example
class Humans(Mammals):
    def __init__(self, name, habitat, birth_num, age, voice_type):
        super().__init__(name, habitat, birth_num, age)
        self.voice_type = voice_type

    def __str__(self):
        return f"{self.name}, {self.habitat}, {self.voice_type}, {self.get_age()}"


joe = Humans("Joe", "Africa", 2, 20, "Speaking")
print(joe.voice_type)
print(joe)


class Whale(Mammals):
    def __init__(self, name, habitat, birth_num, age, voice_type, weight):
        super().__init__(name, habitat, birth_num, age)
        self.voice_type = voice_type
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.voice_type}, {self.weight}kg"


tim = Whale("Tim", "water", 1, 21, "Whistling", 20000)
print(tim)  # Tim, Whistling, 20000kg


class Cat(Mammals):
    def __init__(self, name, habitat, birth_num, age, voice_type, favorite_food):
        super().__init__(name, habitat, birth_num, age)
        self.voice_type = voice_type
        self.favorite_food = favorite_food

    def __str__(self):
        return f"{self.name}, {self.get_age()}, {self.voice_type}, {self.favorite_food}"


kitty = Cat("Kitty", "Human home", 5, 3, "Meow", "fish")
print(kitty)  # Kitty, 3, Meow, fish
