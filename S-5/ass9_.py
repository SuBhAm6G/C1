# Use the functools.partial function to create a new function that multiplies its input by 2. Test the new function with different inputs.
from functools import partial

def multiply(x,y):
    return x*y
double=partial(multiply,y=2)
print(double(8))
print(double(15))