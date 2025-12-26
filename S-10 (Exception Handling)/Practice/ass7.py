# Write a function that takes a list and an index as input and returns the element at the given index. Use try, except, and finally blocks to handle IndexError if the index is out of range and print an appropriate message.
def get_element(lst, index):
    try:
        return lst[index]
    except IndexError as ex:
        print(f"IndexError: {ex}")
        return None
    finally:
        print("The Function Call is complete")

print(get_element([10, 20, 30, 40, 50], 2))
print(get_element([10, 20, 30, 40, 50], 12))