# Write a function that appends a given string to the end of a file named `log.txt`.
def append_str(str):
    with open(r'E:\01_Learning - Udemy\C1\S-9\Practice\log.txt', 'a') as f:
        f.write(str)
append_str("Fourth Line")