l=[1,4,6,2,7,5]
newlist=[]
while l:                                                    # here while l is only true when there is elements inside l,
    minimum=l[0]                                            # and when l becomes empty by removing the elemts through remove
    for i in l:
        if i<minimum:
            minimum=i
    newlist.append(minimum)                        # using this code we can solve (sort) and (find max and min values in a list)
    l.remove(minimum)
print(newlist)