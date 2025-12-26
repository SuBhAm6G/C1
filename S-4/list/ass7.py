# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
import random
lst=[[random.randint(1,20) for x in range(3)] for x in range(3)]
print(lst[1][2])