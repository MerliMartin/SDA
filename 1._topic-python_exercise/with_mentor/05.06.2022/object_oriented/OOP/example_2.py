"""
circle, rectangle
Circumference formula of a circle = c = 2*pie*r
area of circle a = pie*r**2

Area of a rectangle area = a x b
perimeter of a rectangle. perimeter = 2(a+b)
"""
import math

class Circle:
    pie = 3.14  # class variable

    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        return self.pie * self.radius**2

    def diameter_circle(self):
        return 2 * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_rectangle(self):
        return self.width * self.height

    def perimeter_rectangle(self):
        return 2 * (self.width + self.height)

    def diagonal_rectangle(self):
        return math.sqrt(self.height**2 + self.width**2)


x = Circle(5)
y = Rectangle(5, 10)
print(x.area_circle())
print(y.area_rectangle())
print(y.perimeter_rectangle())
print(y.diagonal_rectangle())
print(x.diameter_circle())