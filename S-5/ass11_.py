# Define a function that generates an infinite sequence of Fibonacci numbers. Test by printing the first 10 numbers in the sequence.
def fibo_seq():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

gen=fibo_seq()
for _ in range(10):
    print(next(gen))

