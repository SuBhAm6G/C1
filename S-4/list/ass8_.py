# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 72},
    {'name': 'Charlie', 'score': 95},
    {'name': 'David', 'score': 65},
    {'name': 'Eve', 'score': 78}
]
sorted_students=sorted(students, key=lambda x: x['score'], reverse=True)
print(sorted_students)