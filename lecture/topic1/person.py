from lecture.topic1.address import Address

class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):  # Constructor sets all to no value
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return self.last_name + ", " + self.first_name + " lives at \n" + str(self.address.display())

#Driver
if __name__ == "__main__":
    addy = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
    p = Person('Hammer', 'M', addy)
    print(p.display())
