### Assignment 14: Class with Context Manager

# Create a class named `FileManager` that implements the context manager protocol to open and close a file. Use this class to read the contents of a file.

class FileManager:
    def __init__(self, fname):  # Constructor - stores filename
        self.fname = fname
    
    def __enter__(self):  # Called when entering 'with' block
        self.file = open(self.fname, 'r')  # Opens file and stores it
        return self.file  # Returns file object to use in 'with' block
    
    def __exit__(self, exc_type, exc_value, traceback):  # Called when exiting 'with' block
        print(f"Exception Type: {exc_type}")
        print(f"Exception Value: {exc_value}")
        print(f"Traceback: {traceback}")
        self.file.close()  # Closes the file

# Usage - reads file contents
with FileManager('sample.txt') as file:  # Calls __enter__, assigns returned file to 'file'
    content = file.read()  # Reads the file content
    print(content)  # Prints the content
# __exit__ is automatically called here