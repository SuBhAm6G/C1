# Write a function that reads the contents of a file named `data.txt`. Use try, except, and finally blocks to handle file not found errors and ensure the file is properly closed.
def file_read(filepath):
    try:
        file=open(filepath,'r')
        content=file.read()
        return content
    except Exception as ex:
        print(ex)
    finally:
        try:
            file.close()
        except Exception as ex:
            print(ex)
print(file_read('data.txt'))