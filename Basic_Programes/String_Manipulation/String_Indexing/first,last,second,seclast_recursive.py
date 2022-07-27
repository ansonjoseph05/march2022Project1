s=input("Enter a string: ")    # aabbccddddd
e=""
rec=""
for i in s:
    if i not in e:
        e=e+i    #
    else:
            rec=rec+i
print("Second recursive element is",rec[1])
print("Second last recursive element is",rec[-2])
print("First recursive element is",rec[0])
print("Last recursive element is",rec[-1])