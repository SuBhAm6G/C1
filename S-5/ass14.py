# Define a function that takes a list of mixed data types (integers, strings, and floats) and returns three lists: one containing all the integers, one containing all the strings, and one containing all the floats. Test with different inputs.
def separator(lst):
    int_lst=[]
    str_lst=[]
    float_lst=[]
    for x in lst:
        if isinstance(x,int):
            int_lst.append(x)
        elif isinstance(x,str):
            str_lst.append(x)
        elif isinstance(x,float):
            float_lst.append(x)
    return int_lst,str_lst,float_lst

lst=[1,2,3,'4','abc',5.8,9.0,9]
print(separator(lst))
