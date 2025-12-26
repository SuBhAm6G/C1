# Write a function that prompts the user to enter an integer. Use try, except, and finally blocks to handle ValueError if the user enters a non-integer value and print an appropriate message.
def enter_int():
    flag=0
    try:
        n=int(input("Enter an input: "))
        flag=1
    except ValueError as ex:
        print(ex)
    finally:
        if flag: print("Success")
        else: print("Failed")
enter_int()
