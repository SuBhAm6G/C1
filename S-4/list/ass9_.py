# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.
def transpose(matrix):
    l=len(matrix[0])
    tr=[[matrix[j][i] for j in range(l)]for i in range(l)]
    return tr
lst=[[input() for _ in range(3)] for _ in range(3)]
for row in lst:
    print(row)
print()
tr=transpose(lst)
for row in tr:
    print(row)