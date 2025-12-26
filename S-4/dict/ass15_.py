# Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.
import json

book = {
    'title': 'The Hitchhiker\'s Guide to the Galaxy',
    'author': 'Douglas Adams',
    'year': 1979,
    'genre': 'Science Fiction'
}

json_string = json.dumps(book, indent=2)
print(json_string)