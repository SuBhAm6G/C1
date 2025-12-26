# Use the `os` module to create a new directory, list the contents of the current directory, and remove the newly created directory.
import os
try:
    os.mkdir("New_dir")
except:
    print("File Already exists")
print(os.listdir("./practice"))
os.rmdir("New_dir")