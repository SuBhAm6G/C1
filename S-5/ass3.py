# Define a function that takes a variable number of keyword arguments and returns a dictionary containing only those key-value pairs where the value is an integer. Test the function with different inputs.
def func(**kwargs):
    dic={x:y for x,y in kwargs.items() if isinstance(y,int)}
    return dic

print(func(x=78.6,z=89))