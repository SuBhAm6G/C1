# Write a function that takes a dictionary and a key as input and returns the value associated with the key. Use try, except, and finally blocks to handle KeyError if the key is not found in the dictionary and print an appropriate message.
def func(dic,key):
    try:
        return dic[key]
    except KeyError as ex:
        print(f"the Key {ex} doesn't exist")
        return None
    finally:
        print("The Function Call is complete")
print(func({1:2,3:4},1))
print(func({1:2,3:4},5))