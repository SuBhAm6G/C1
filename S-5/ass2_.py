# Define a function that takes two arguments, a and b, where b is a dictionary with a default value of an empty dictionary. The function should add a new key-value pair to the dictionary and return it. Test the function with different inputs.
def add_to_dict(a, b={}):
    b[a] = a
    return b

# Test cases
print(add_to_dict("key1"))
print(add_to_dict("key2", {"existing_key": "value"}))
my_dict = {}
print(add_to_dict("key3", my_dict))
print(my_dict)
dic={'lec1':78}
print(add_to_dict('lec2',dic))