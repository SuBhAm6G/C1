# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
dic={x:x*x for x in range(1,11)}
dic[11]=121
del dic[1]
print(dic)