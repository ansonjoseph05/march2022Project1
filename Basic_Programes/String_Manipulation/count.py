s="aaabbbcccabc"
n=input("Enter a string: ")
count=0
for i in s:
    if n in i:
        count=count+1
print(count)