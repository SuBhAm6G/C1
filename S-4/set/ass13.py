# Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.
set1=set(range(1,6))
set2=set(range(4,9))
print('set1 before update: ',set1)
set1.symmetric_difference_update(set2)
print('set1 after update: ',set1)