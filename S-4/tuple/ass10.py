# Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
tpl=tuple(range(1,6))
lst=list(tpl)
lst.append(6)
tpl=tuple(lst)
print(tpl)