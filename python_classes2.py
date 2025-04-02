from unittest import results


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        results = 22/7* self.radius **2*22/7* self.radius * self.height
        print(f"Area is: {results}")

    def volume(self):
        results = (22/7* self.radius **2*2*22/7* self.radius * self.height)
        print(f"Volume is: {results}")

    def print_details(self):
        print(f"radius is: {self.radius} and height : {self.height}")
