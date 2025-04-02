from python_classes2 import Cylinder

class Person:
    def __init__(self, name, age):
        print("creating a person")
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"hi there, I am {self.name} and I am {self.age} years old")

p1 = Person(name="John", age=36)
p2 = Person(name="Jared", age=26)
p3 = Person(name="Juma", age=32)

p1.say_hello()
p2.say_hello()
p3.say_hello()

name = "Jay"
name.upper()

c1 = Cylinder()
c2 = Cylinder()

c1.area()
c1.volume()
c1.print_details
