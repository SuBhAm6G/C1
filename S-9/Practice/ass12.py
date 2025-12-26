# Write a function that reads a binary file named `image.bin` and writes its contents to another binary file named `copy_image.bin`.
def copy_btwn_files_bin(source_path,output_path):
    with open(source_path,'rb') as f1:
        content=f1.read()
        with open(output_path,'wb') as f2:
            f2.write(content)