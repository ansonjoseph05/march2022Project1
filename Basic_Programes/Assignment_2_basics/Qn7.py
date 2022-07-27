# 7. Remove vowels from the input string given by user?

s=input("Enter sring: ")
v="aeiou"
e=" "
for i in s:
    if i not in v:
        e=e+i
print(e)
