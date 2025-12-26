# Write a function that splits a large file named `large.txt` into smaller files of 100 lines each.
def split_file(filename, lines_per_file):
    with open(filename,'r') as file:
        lines=file.readlines()
    for i in range(0,len(lines),lines_per_file):
        with open(f'{filename}_part{i//lines_per_file +1}.txt', 'w') as part_file:
            part_file.writelines(lines[i:i+lines_per_file])
split_file('sample.txt',3)