#n1=0
#n2=1
#for i in range(10):  #i=0,1,...,9
#    print(n1)
#    nth=n1+n2
#    n1=n2
#    n2=nth


#explain the working of the given code
for i in range(2):
    if i==2:
        break
    print(i)
    for j in range(5):
        if i==3:
            break
        else:
            print(j)

