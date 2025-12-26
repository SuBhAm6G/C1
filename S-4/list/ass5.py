# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
lst=list(range(1,21))
lst2=[x for x in lst if (x%2==0)]
print(lst2)