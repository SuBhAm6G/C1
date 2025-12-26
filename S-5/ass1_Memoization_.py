# Define a recursive function to calculate the nth Fibonacci number using memoization. Test the function with different inputs.
def fibo(n, memo=None):
    if memo is None:
        memo={}
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if n==1:
        return 1
    memo[n]=fibo(n-1,memo)+fibo(n-2,memo)
    return memo[n]

print([fibo(x) for x in range(5)])
    

#Default Memoization
from functools import lru_cache

@lru_cache(None)
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

print([fibo(x) for x in range(5)])