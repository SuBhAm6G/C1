# Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.
set1=set(x*x for x in range(1,11))
print(set1)