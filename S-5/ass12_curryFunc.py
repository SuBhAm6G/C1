# Define a curried function that takes three arguments, one at a time, and returns their product. Test the function by providing arguments one at a time.
def curried_mul(a):
    def inner1(b):
        def inner2(c):
            return a*b*c
        return inner2
    return inner1

res=curried_mul(2)(3)(4)
print(res)