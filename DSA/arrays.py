
from array import * # from array import all 

val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' is signed integer (usually 4 bytes)

# for i in range(0,6): # prints upto 6
for i in range(0,len(val)):
    print(val[i],end=" ")
print("\n")
for x in val: # enhance for loop to print the array
    print(x,end=" , ")