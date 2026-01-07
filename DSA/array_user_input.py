from array import *

a = array('i',[])

b = (int(input("Enter how many  numbers :")))

for i in range(0, b):
    a.append(int(input("Enter next number :")))

for x in a:
    print(x,end=" ")