### Assignment 11: Abstract Base Class

# Create an abstract base class named `Shape` with an abstract method `area`. Create derived classes `Circle` and `Square` that implement the `area` method. Create objects of the derived classes and call the `area` method.
from abc import ABC,abstractmethod
class Shape(ABC): #Abstract Base Class
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.__radius=radius
    def area(self):
        print(f"The area of circle is {3.14*self.__radius**2}")
class Square(Shape):
    def __init__(self,length):
        self.__length=length
    def area(self):
        print(f"The area of square is {self.__length**2}")
circle = Circle(5)
circle.__radius=6 ##it will not change the radius as it is private attribute
circle.area()  # The area of circle is 78.5
square = Square(4)
square.area()  # The area of square is 16
