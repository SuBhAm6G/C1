# Print the value of the key 5 and the keys of the dictionary created in Assignment 1.
dic={x:x*x for x in range(1,11)}

# print(dic[5])
print(dic.get(5,'Not Available'))