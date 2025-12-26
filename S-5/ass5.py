# Define a function that returns another function. The returned function should take an integer and return its square. Test the returned function with different inputs.
def sqr(x):
    return x*x
def func(x):
    return sqr(x)

print(func(5))