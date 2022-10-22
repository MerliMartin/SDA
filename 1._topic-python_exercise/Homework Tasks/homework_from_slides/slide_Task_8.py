"""
Create a Rectangle class whose attributes will be the height and width of
the figure. Implement methods to measure the perimeter and area of a
rectangle.
Then create a Square class, remembering that every square is a
rectangle, but not every rectangle is a square
"""


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter_of_rectangle(self):
        return 2 * (self.height + self.width)

    def area_of_rectangle(self):
        return self.height * self.width

    def __str__(self):
        return f"Rectangle area is {self.area_of_rectangle()} and the perimeter is {self.perimeter_of_rectangle()} " \
               f"when the height is {self.height} and width is {self.width}!"


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return f"Square area is {self.area_of_rectangle()} and the perimeter is {self.perimeter_of_rectangle()} " \
               f"when the side length of square is {self.height}"


def check_parameters(given_height, given_width):
    if given_height == given_width:
        print("You have Square!")
        return Square(given_height)
    else:
        print("You have Rectangle")
        return Rectangle(given_height, given_width)


print(Rectangle(2, 5))
user_rectangle_height = int(input("What is your rectangle height?: "))
user_rectangle_width = int(input("What is your rectangle width?: "))
print(check_parameters(user_rectangle_height, user_rectangle_width))
