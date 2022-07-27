# Qn1. Code to find sum of positive numbers between -5 to 10 using function with argument?

def possum(n1,n2):
    sum=0
    for i in range(n1,n2+1):
        if i>0:
            sum+=i
    print(sum)
possum(-5,10)


