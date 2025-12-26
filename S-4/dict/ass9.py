# Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.
dic={x:(x,x*x) for x in range(1,6)}
print(dic)