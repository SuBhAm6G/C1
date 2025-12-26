# Define a function that composes two functions, f and g, such that the result is f(g(x)). Test with different functions f and g.
def compose(f,g):
    return lambda x: f(g(x))
f=lambda x:x*x+3
g=lambda y:8*(y**3)-7
h=compose(f,g)
print(h(3.5))
print(h(9))