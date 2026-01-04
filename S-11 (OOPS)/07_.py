# Create a class named `Address` with attributes `street`, `city`, and `zipcode`. Create a class named `Person` that has an `Address` object as an attribute. Create an object of the `Person` class and print its address.
class Address:
    def __init__(self,street,city,zipcode):
        self.street=street
        self.city=city
        self.zipcode=zipcode
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
address=Address("123 Main St","Springfield","12345")
person1=Person("John Doe",30,address)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
print(f"Address: {person1.address.street}, {person1.address.city}, {person1.address.zipcode}")
    
        