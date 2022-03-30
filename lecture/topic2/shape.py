class InvalidColorError(Exception):
    """InvalidColorError is derived class of Excpetion base class"""
    pass

class Shape:
    """Shape class"""
    colors = ['BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'RED', 'YELLOW']

    def __init__(self, color='BLUE'):
        self._color = color

    def change_color(self, new_color):
        if new_color not in self.colors:
            raise InvalidColorError
        self._color = new_color

    def display_color(self):
        return str(self._color)

if __name__ == "__main__":
    # Driver
    my_shape = Shape()
    color = 'blue'
    try:
        my_shape.change_color(color)
    except InvalidColorError:
        print("Color is not valid:", color)
    print("Color is", my_shape.display_color())
