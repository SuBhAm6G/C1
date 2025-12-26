# Define a custom exception named `NegativeNumberError`. Write a function that raises this exception if a negative number is encountered in a list. Use try, except, and finally blocks to handle the custom exception and print an appropriate message.

class NegativeNumberError(Exception):
    pass
def check_for_negatives(lst):
    try:
        for num in lst:
            if num<0:
                raise NegativeNumberError(f"Negative number found: {num}")
    except Exception as e:
        print(e)
    finally:
        print("The Function Call is complete")

# check_for_negatives([1, 2, 3, -4, 5])
# check_for_negatives([1, 2, 3, 4, 5])
# check_for_negatives([1, 2, 3, 4, 'a'])
check_for_negatives([-1, -2, -3])
