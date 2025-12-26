# Write a function that takes two integers as input and returns their division. Use try, except, and finally blocks to handle division by zero and print an appropriate message.
def division(a,b):
    try:
        res=a/b
        return res
    except ZeroDivisionError as e:
        print(e)
        return None
    finally:
        print("The Function Call is complete")
print(division(10,2))
print(division(10,0))

