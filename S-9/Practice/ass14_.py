# Write a function that reads a JSON file named `data.json` and prints its contents as a Python dictionary.
import json
def read_json(file_path):
    with open(file_path,'r') as f:
        content=json.load(f)
        return content
print(read_json("data.json"))
