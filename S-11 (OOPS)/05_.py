### Assignment 5: Class Inheritance

# Create a base class named `Person` with attributes `name` and `age`. Create a derived class named `Employee` that inherits from `Person` and adds an attribute `employee_id`. Create an object of the derived class and print its attributes.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age) #super to call parent class constructor
        self.employee_id=employee_id

employee1=Employee("Alice",20,"12345")
print(employee1.name)
print(employee1.age)
print(employee1.employee_id)
        