# Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.
nested_lst=[[input() for _ in range(3)] for _ in range(3)]
flattended_lst=[]
for i in range(3):
    flattended_lst.append(nested_lst[i])

for row in nested_lst:
    print(row)
print()
print(flattended_lst)
