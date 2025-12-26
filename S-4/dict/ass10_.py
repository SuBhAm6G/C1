# Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.
dic={x:x**2 for x in range(1,6)}
print(dic)
print(tuple(dic.items()))