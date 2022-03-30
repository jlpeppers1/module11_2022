from lecture.topic3.shape import Shape
from lecture.topic3.shape import InvalidColorError

class Rectangle(Shape):   # Base class is Shape
    """Rectangle derived class of Shape base class"""
    def __init__(self, c='RED', l=0, w=0):  # default values
        super().__init__(c)  # calls the base constructor
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def display_color(self):
        return str('Rectangle color ' + self.color)
