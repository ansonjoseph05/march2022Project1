l=[1,2,3,3,4,5,5,6,6,7,8]          #imp problem , study well
n=[]
dup=[]
for i in l:
    if i not in n:
        n.append(i)
    else:
        dup.append(i)
print(dup)