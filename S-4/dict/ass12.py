# Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.
dic={x:x**2 for x in range(1,6)}
new_dic={y:x for x,y in dic.items()}
print(new_dic)