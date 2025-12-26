# Write a function that rotates a list by n positions. Print the original and rotated lists.
def rotate(lst,n,r):
    new_lst=lst[(n-r):n]+lst[0:(n-r)]
    return new_lst
n=int(input("Enter number of elements you want to enter: "))
lst=[input() for i in range(n)]
r=int(input("Enter number of rotations: "))
rotated_lst=rotate(lst,n,r)
print("Original List: ",lst)
print("Rotated List: ",rotated_lst)