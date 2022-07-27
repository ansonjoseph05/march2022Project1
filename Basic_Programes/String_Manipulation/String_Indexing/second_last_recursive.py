s=input("Enter a string: ")      #imp interview qns
e=""
rec=""
for i in s:
    if i not in e:
        e=e+i
    elif i not in rec:
        rec=rec+i
print("second recursive element is ",rec[1])
print("second last recursive element is ",rec[-2])



