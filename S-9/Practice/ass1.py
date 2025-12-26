# Write a function that reads the contents of a file named `sample.txt` and prints each line.
path=r'E:\01_Learning - Udemy\C1\S-9\sample.txt'
with open(path, 'r') as f:
    for line in f:
        print(line.strip())