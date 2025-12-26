# Write a function that reads the contents of a file named `reverse.txt` and prints each line in reverse order.
def reverse_line(file_path):
    with open(file_path,'r') as f:
        for line in f:
            print(line[::-1].strip())
reverse_line(r'./Practice/log.txt')