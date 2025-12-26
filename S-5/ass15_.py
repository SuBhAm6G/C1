# Define a function that maintains state between calls using a mutable default argument. The function should keep track of how many times it has been called. Test by calling the function multiple times.
def tripler(counter={'count':0}):
    counter['count']+=1
    return lambda x:x*3,counter['count']

for _ in range(5):
    t,c=tripler()
    print(f"{t(5)} & {c}")