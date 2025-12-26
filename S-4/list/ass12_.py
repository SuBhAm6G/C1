# Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.
lst1=['a','b','c','d','e']
lst2=[1,2,3,4,5]
zipped_list=list(zip(lst1,lst2))
print(zipped_list)