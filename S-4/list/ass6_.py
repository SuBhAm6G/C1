# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
import random
lst=[random.randint(1,100) for _ in range(10)]
print(lst)
asc_lst=sorted(lst)
desc_lst=sorted(lst, reverse=True)
print("Ascending:", asc_lst)
print("Descending:", desc_lst)
lst=list(set(lst))
print(lst)