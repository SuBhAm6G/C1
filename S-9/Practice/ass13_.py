# Write a function that reads a CSV file named `data.csv` and prints its contents as a list of dictionaries.
import csv
def read_csv_as_dicts(file_path):
    with open(file_path,'r') as csvfile:
        reader_csv=csv.DictReader(csvfile)
        return list(reader_csv)
print(read_csv_as_dicts("test.csv"))
