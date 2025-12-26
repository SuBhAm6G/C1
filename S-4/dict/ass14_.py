# Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.

#Inefficent
# def func(txt):
#     txt2=txt.strip()
#     dic={c:txt2.count(c) for c in txt2}
#     return dic
# txt="I'm learning Python programming with python interpreter"
# print(func(txt))

#Efficient
def func(txt):
    txt2=txt.lower().strip()
    freq={}
    for char in txt2:
        if(char in freq):
            freq[char]+=1
        else:
            freq[char]=1
    return freq

txt="I'm Learning Python programming with python interpreter"
print(func(txt))