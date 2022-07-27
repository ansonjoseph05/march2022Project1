s={1,-4,3,5,-7,-8,3,7}
pos=set()
neg=set()
for i in s:
    if i>0:
        pos.add(i)
    else:
        neg.add(i)
print(pos)
print(neg)

