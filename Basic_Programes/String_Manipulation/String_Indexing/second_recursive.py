s=input("Enter a string: ")
e=""
rec=""
for i in s:
    if i not in e:
        e=e+i
    elif i not in rec:
        rec=rec+i
print("second recursive element is ",rec[1])


