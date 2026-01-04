# Create a class named `Counter` with a class variable `count`. Each time an object is created, increment the count. Add a method to get the current count. Create multiple objects and print the count.

class Counter:
    count=0
    def __init__(self):
        Counter.count+=1
    @classmethod
    def current_count(self):
        print("Current count:",Counter.count)

counter1=Counter()
counter2=Counter()
counter3=Counter()
counter1.current_count()