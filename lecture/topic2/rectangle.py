from lecture.topic2.shape import Shape


class Rectangle(Shape):   # Base class is Shape
    """Rectangle derived class of Shape base class"""
    def __init__(self, c='RED', l=0, w=0):  # default values
        super().__init__(c)  # calls the base constructor
        self._length = l
        self._width = w

    def area(self):
        return self._length * self._width

    def display_color(self):
        return str('Rectangle color ' + self._color)

if __name__ == "__main__":
    # Driver
    my_shape = Shape()
    my_rectangle = Rectangle('BLUE', 5, 10)
    # Tests if object my_shape is Shape
    print('my_shape is a Shape:', isinstance(my_shape, Shape))
    # Tests if object my_rectangle is Shape
    print('my_rectangle is a Shape:', isinstance(my_rectangle, Shape))
    # Tests if object my_shape is Rectangle
    print('my_shape is a Rectangle:', isinstance(my_shape, Rectangle))
    # Tests if object my_rectangle is Rectangle
    print('my_rectangle is a Rectangle:', isinstance(my_rectangle, Rectangle))

