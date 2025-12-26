# Write a program that calculates the sum of the digits of a number input by the user using a while loop.
n=int(input('n= '))
n=abs(n)
sum=0
while(n!=0):
    sum+=n%10
    n//=10
print(sum)