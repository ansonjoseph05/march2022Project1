s=input("Enter a string: ")    #aabbcc
e=""
rec=""
for i in s:
    if i not in e:
        e=e+i     #abc
    else:
        rec=rec+i
print("last recursive element is ",rec[-1])


