# Create a class named `Vector` with attributes `x` and `y`. Overload the `+` operator to add two `Vector` objects. Create objects of the class and test the operator overloading.
class Vector:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def __add__(self,vec2): #custom method
        return Vector(self.__x+vec2.__x, self.__y+vec2.__y)
    def __sub__(self,vec2):
        return Vector(self.__x-vec2.__x, self.__y-vec2.__y)
    def __str__(self):
        return f"Vector({self.__x}, {self.__y})"
v1=Vector(2,3)
v2=Vector(4,3)
v3=v1-v2
print(v3)
v4=v1+v2
print(v4)
