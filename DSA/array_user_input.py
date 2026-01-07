# from array import *

# a = array('i',[])

# b = (int(input("Enter how many  numbers :")))

# for i in range(0, b):
#     a.append(int(input("Enter next number :")))

# for x in a:
#     print(x,end=" ")

from array import *
arr = array('i',[1,2,34,23,45,43,67,32])

a = arr.index(43)
print(a)