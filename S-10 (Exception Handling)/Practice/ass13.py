# Write a function that uses a list comprehension to convert a list of strings to integers. Use try, except, and finally blocks within the list comprehension to handle ValueError and print an appropriate message.
def str_to_int(lst):
    try:
        int_lst=[int(x) for x in lst]
        return int_lst
    except TypeError:
        print("Error: Non-string value encountered in the list.")
        return None
    except ValueError as ex:
        print(f"ValueError: {ex}")
        return None
    finally:
        print("Conversion attempt complete.")

print(str_to_int(['1', '2', '3']))
print(str_to_int(['1', 'a', '3']))
print(str_to_int([1, 2, 3]))
