# Write a program that calculates the factorial of a number input by the user using a while loop.
n=int(input('n= '))
result=1
while (n!=0):
    result*=n
    n-=1
print(result)