# Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.
def func(tpl):
    max_element=max(tpl)
    min_element=min(tpl)
    sum_element=sum(tpl)
    return max_element,min_element,sum_element

n=int(input("n= "))
tpl=()
for i in range(n):
    a=int(input(f"{i+1}= "))
    tpl+=(a,)
max_element,min_element,sum_element=func(tpl)
print("Max:",max_element)
print("Min:",min_element)
print("Sum:",sum_element)
