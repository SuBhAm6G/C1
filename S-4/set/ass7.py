# Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.
set1=set(range(1,6))
set2=set(range(1,4))
if(set2.issubset(set1) and set1.issuperset(set2)):
    print(set1,set2)