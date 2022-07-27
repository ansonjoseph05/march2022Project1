#first recursive element
s=input("Enter String: ")    #aabbcc
e=""
for i in s:
    if i not in e:       #abc
        e=e+i
    else:
        print("First recursive element: ",i)
        break

