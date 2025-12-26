# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
dic1={x:x*x for x in range(1,6)}
dic2={x:x*x for x in range(6,11)}
dic3={**dic1,**dic2}
print(dic3)