### Assignment 6: Method Overriding

# In the `Employee` class, override the `__str__` method to return a string representation of the object. Create an object of the class and print it.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age) #super to call parent class constructor
        self.employee_id=employee_id
    def __str__(self):
        return f"Employee Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}"
employee1=Employee("Alice",20,"12345")
print(employee1)        

