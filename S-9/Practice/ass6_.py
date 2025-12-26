# Write a function that finds and replaces all occurrences of a given word in a file named `data.txt` with another word.
def replace_word_inFile(word,replacewith):
    with open(r'E:\01_Learning - Udemy\C1\S-9\Practice\log.txt', 'r+') as f:
        content=f.read()
        content=content.replace(word,replacewith)
        f.seek(0)
        f.write(content)

replace_word_inFile("LIne", "Wow")