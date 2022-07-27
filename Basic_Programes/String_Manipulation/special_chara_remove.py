s=input("Enter a string: ")
symbol="`~!@#$%^&*()_-+=\|}]{[':;?/>.<,"
new=""
for i in s:
    if i not in symbol:
        new=new+i
print(new)
        