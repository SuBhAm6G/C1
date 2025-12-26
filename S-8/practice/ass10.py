# Use the `random` module to generate a list of 5 random numbers between 1 and 50 and shuffle the elements of a list.
import random
random_numbers=[random.randint(1,50) for _ in range(5)]
print("Random Numbers:", random_numbers)
random.shuffle(random_numbers)
print("Shuffled List:", random_numbers)
