s="Luminar Technolab"
e=input("Enter single string: ")
new=""
for i in s:
    if i not in e:
        new=new+i
print(new)