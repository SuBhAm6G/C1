# Write a function that copies the contents of a file named `source.txt` to a new file named `destination.txt`.
def copy_btwn_files(source_path,output_path):
    with open(source_path,'r') as f1:
        content=f1.read()
        with open(output_path,'w+') as f2:
            f2.write(content)

source_file_path = r'E:\01_Learning - Udemy\C1\S-9\sample.txt'
destination_file_path = r'E:\01_Learning - Udemy\C1\S-9\Practice\destination.txt'
copy_btwn_files(source_file_path, destination_file_path)