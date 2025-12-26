# Write a function that attempts to parse a JSON string. Use try, except, and finally blocks to handle JSONDecodeError if the string is not a valid JSON and print an appropriate message.
import json
def parse_json(json_string):
    try:
        data=json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(e)
        return None
    
print(parse_json('{"name": "John", "age": 30}'))  
print(parse_json('Invalid JSON'))