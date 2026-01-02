### Assignment 2: Methods in Class

# Add a method named `start_engine` to the `Car` class that prints a message when the engine starts. Create an object of the class and call the method.
import datetime
class Car:
    def start_engine(self):
        print(f"Engine started at {datetime.datetime.now()}")

tata=Car()
tata.start_engine()