# Write a function that takes a list of integers and returns their sum. Use try, except, and finally blocks to handle TypeError if a non-integer value is encountered and print an appropriate message.

def sum_values(lst):
    total=0
    try:
        for item in lst:
            total+=item
    except TypeError as ex:
        print(f"Error: {ex}")
        total=None
    finally:
        print("The Function Call is complete")
    return total
print(sum_values([1,2,3,4,5]))
print(sum_values([1,2,'a',4,5]))