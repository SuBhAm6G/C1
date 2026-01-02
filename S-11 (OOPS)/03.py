### Assignment 3: Class with Constructor

# Create a class named `Student` with attributes `name` and `age`. Use a constructor to initialize these attributes. Create an object of the class and print its attributes.

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

student1=Student("Alice",20)
print(student1.name)
print(student1.age)
student2=Student("Bob",22)
print(student2.name)
print(student2.age)
