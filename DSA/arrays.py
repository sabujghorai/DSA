import array

val = array.array('i',[10,11,20,22,25,34,54,23])  # 'i' is signed integer (usually 4 bytes)

for i in range(0,8):
    print(val[i],end=" ")