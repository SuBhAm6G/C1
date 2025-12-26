# Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.
def intersect(lst1,lst2):
    lst=[x for x in lst1 if x in lst2]
    return lst
lst1=[12,14,67,34]
lst2=[14,78,34,14]
result=intersect(lst1,lst2)
print("Intersected List: ",list(set(result)))