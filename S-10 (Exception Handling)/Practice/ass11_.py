# Write a function that calls another function which may raise an exception. Use try, except, and finally blocks to handle the exception and print an appropriate message.

def another_function():
    raise KeyError("An Error Occured in 'another_function'")
def a_function():
    try:
        another_function()
    except KeyError as e:
        print(f"Error: {e}")
    finally:
        print("Execution complete.")

a_function()