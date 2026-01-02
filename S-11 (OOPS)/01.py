### Assignment 1: Basic Class and Object Creation

# Create a class named `Car` with attributes `make`, `model`, and `year`. Create an object of the class and print its attributes.
class Car:
    def __init__(self,maker,model,year):
        self.maker=maker
        self.model=model
        self.year=year

car1=Car("Tata","Cierra",2025)
print(car1.maker)
print(car1.model)
print(car1.year)
    


