# Write a function that merges the contents of multiple files into a single file named `merged.txt`.
def merge_files(*arg):
    with open("merged.txt",'w') as outfile:
        for fname in arg:
            with open(fname, 'r') as infile:
                outfile.write(infile.read()+'\n')
merge_files('./Practice/log.txt', 'log.txt', './Practice/output.txt')