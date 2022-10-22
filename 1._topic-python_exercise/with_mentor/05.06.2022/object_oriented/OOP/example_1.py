class Animal:
    def __init__(self, name, no_of_legs):
        self.name = name
        self.no_of_legs = no_of_legs

    def print_name(self):
        print(self.name)


puppy = Animal("Puppy", 4)
bingo = Animal("Bingo", 4)
spider = Animal("Ringo", 7)

print(f"My dog name is {puppy.name} and he has {puppy.no_of_legs} legs.")
print(f"My spider name is {spider.name} and he has {spider.no_of_legs} legs!")
puppy.print_name()
puppy.no_of_legs = 5
print(puppy.no_of_legs)