# Write a function that performs nested exception handling. It should first attempt to convert a string to an integer, and then attempt to divide by that integer. Use nested try, except, and finally blocks to handle ValueError and ZeroDivisionError and print appropriate messages.
def func(s):
    try:
        val=int(s)
        res=100/val
        return res
    except ValueError as ex:
        print(ex)
        return None
    except Exception as ex:
        print(ex)
        return None

print(func('10'))
print(func('0'))
print(func('a'))

