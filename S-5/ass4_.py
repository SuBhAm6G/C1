# Define a function that takes another function as a callback and a list of integers. The function should apply the callback to each integer in the list and return a new list with the results. Test with different callback functions.
def sqr(x):
    return x*x
def func(callback,lst):
    return [callback(x) for x in lst]
lst=[1,2,3,4,5]
print(func(sqr,lst))
