# Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
import random
matrix=tuple(tuple(random.randint(1,100) for _ in range(3))for _ in range(3))
print(matrix)
print(matrix[1][2])