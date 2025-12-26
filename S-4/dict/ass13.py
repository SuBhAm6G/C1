# Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.
lst=[]
dic={x:lst for x in range(5)}
print(dic)
lst.append(69)
print(dic)