import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...
        

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        print(f"Area is: {self.width * self.height}")

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def area(self):
        print(f"Area is: {math.pi * self.radius**2}")

# - - -

def main():
    s1 = Rectangle(3,4)
    s2 = Circle(7)

    s1.area()
    s2.area()

if __name__ == "__main__":
    main()