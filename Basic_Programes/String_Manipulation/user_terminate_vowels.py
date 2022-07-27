s=(input("Enter a string: "))
v="aeiou"
new=""
for i in s:
    if i not in v:
        new=new+i
print(new)
