# Define a higher-order function that takes two functions, a filter function and a map function, along with a list. The higher-order function should first filter the list using the filter function and then apply the map function to the filtered list. Test with different filter and map functions.
import re
def Valid_Names(name):
    if(len(name.split( ))!=2):
        return False
    if re.search(r'[^a-zA-Z]', name.replace(" ","")):
        return False
    else:
        return True
def abbreviate(name):
    acronym=''.join(words[0].upper() for words in name.split())
    return acronym

def func(filtering,mapping,lst):
    return [mapping(x) for x in lst if filtering(x)]

names=['Ramesh Haldar', 'Xy09', 'Anita Mishra', 'John_Doe', 'Alice123', 'Bob', 'Elizabeth Ilynov']
print(func(Valid_Names,abbreviate,names))