class Car:

    def __init__(self, brand, colour, wheels=4):
        self.brand = brand
        self.colour = colour
        self.wheels = wheels

    def car_crash(self):
        self.brand = "Unidentifiable"
        self.colour = "Unidentifiable"
        self.wheels = 0

    def __str__(self):
        return "Brand: {0.brand}, Colour: {0.colour}, Wheels: {0.wheels}".format(self)


class Convertable(Car):

    def __init__(self, name, colour):
        super().__init__(self, name, colour, wheels=4)

    def __str__(self):
        return "Brand: {0.brand}, Colour: {0.colour}, Wheels: {0.wheels}".format(self)