# Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.
dic={x:x**2 for x in range(1,11)}
new_dic={p:q for p,q in dic.items() if p%2==0}
print(new_dic)