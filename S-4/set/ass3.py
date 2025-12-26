# Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.
set1=set(range(1,6))
set2=set(2*x for x in range(1,6))
print('set1: ',set1)
print('set2: ',set2)
print('union: ',set1.union(set2))
print('intersection: ',set1.intersection(set2))
print('difference: ',set1.difference(set2))
print('symmetric difference: ',set1.symmetric_difference(set2))