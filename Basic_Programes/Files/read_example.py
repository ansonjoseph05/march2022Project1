f=open('example.txt','r')
for i in f:
    data=i.rstrip("\n")       # this step is used to strip the empty line between the contents in the file
    print(data)