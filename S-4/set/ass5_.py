# Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.
set1=set(range(1,11))
set2=set(x for x in set1 if (x%2==0))
print(set2)