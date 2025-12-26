# Write a function that attempts to write a list of strings to a file. Use try, except, and finally blocks to handle IOError and ensure the file is properly closed.
def write_to_file(filepath,lst):
    try:
        file=open(filepath,'w')
        for item in lst:
            file.write(item+'\n')
    except IOError:
        print("IOError: An error occurred while writing to the file.")
    finally:
        try:
            file.close()
        except:
            pass
write_to_file('data.txt',['1','2','3'])
write_to_file('nonexistent_directory/data.txt',['1','2','3'])
