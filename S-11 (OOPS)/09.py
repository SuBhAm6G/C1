# Create a class named `MathOperations` with a static method to calculate the square root of a number. Call the static method without creating an object.
import math
class MathOperations:
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)
result=MathOperations.sqrt(16)
print("Square root:",result)