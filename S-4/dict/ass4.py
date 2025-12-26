# Iterate over the dictionary created in Assignment 1 and print each key-value pair.
dic={x:x*x for x in range(1,11)}

for key,value in dic.items():
    print(f'{key}:->{value}')