class Parent:
    def __init__(self,name,phn):
        self.name=name
        self.phn=phn
    def printpa(self):
        print(self.name,self.phn)
f=open('parent.txt','r')
for i in f:
    data=i.rstrip("\n").split(",")
    # print(data)
    name=data[0]
    phn=data[1]
    pa=Parent(name,phn)
    pa.printpa()
