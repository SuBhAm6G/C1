# Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.
lst=list(range(1,11))
print("Original list: ",lst)
del lst[6]
del lst[4]
del lst[2]
lst.insert(5, 99)
print("Modified list: ",lst)