# Write a function that writes a list of strings to a file named `output.txt`, with each string on a new line.
def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as f:
        for item in data_list:
            f.write(item + '\n')

output_file_path = r'E:\01_Learning - Udemy\C1\S-9\Practice\output.txt'
my_list = ["This is the first line.", "This is the second line.", "And this is the third."]
write_list_to_file(output_file_path, my_list)
