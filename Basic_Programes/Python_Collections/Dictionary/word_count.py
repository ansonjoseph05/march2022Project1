s="hello hi hello"
count={}
d=s.split(" ")                        # s.split is inbuilt function to split string
for i in d:
    if i not in count:                 # almost all logic in dictionary is coming here
        count.update({i:1})
    else:
        val=count[i]
        val=val+1
        count.update({i:val})
print(count)




