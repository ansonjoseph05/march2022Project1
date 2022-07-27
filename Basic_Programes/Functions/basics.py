#functions


# 1. def variable to repeatedly using the output

#def add():                                 #function without argument
#    n1=int(input("Enter a number :"))
#    n2=int(input("Enter a number :"))
#    print(n1+n2)
#add()
#add()
#add()


#function with argument
#def add(n1,n2):
#    print(n1+n2)
#n01=int(input("Enter n01 : "))
#n02=int(input("Enter n02 : "))
#add(n01,n02)
#n1=int(input("Enter n1 : "))
#n2=int(input("Enter n2 : "))
#add(n1,n2)


#function without argument
#function with argument



#function with argument and return type

#def add(n1,n2):
#    return n1+n2
#n1=int(input("Enter number : "))
#n2=int(input("Enter number : "))
#print("sum is",add(n1,n2))




def pos_neg(n):
    if n>0:
        return "Positive"
    elif n==0:
        return "Zero"
    else:
        return "Negative"
n=int(input("Enter a number : "))
print(pos_neg(n))
