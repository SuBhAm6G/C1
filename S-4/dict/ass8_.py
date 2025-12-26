# Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.
dic={x:[y*x for y in range(1,6)] for x in range(1,6)}
print(dic)