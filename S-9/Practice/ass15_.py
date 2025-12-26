# Write a function that attempts to read a file named `protected.txt` and handles any permission errors gracefully by printing an error message.
def read_protected_file(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"File Not Found Error: {e}")

read_protected_file('protected.txt')