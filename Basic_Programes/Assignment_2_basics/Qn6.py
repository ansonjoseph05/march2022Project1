# 6. create a calculator with functions(addition,subtraction,multiplication,division,floor division,exponent)?

def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mul(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)
def fldiv(n1,n2):
    print(n1//n2)
def exp(n1,n2):
    print(n1**n2)
while True:
    option=int(input("Select options \n1.add\n2.sub\n3.mul\n4.div\n5.fldiv\n6.exp\n7.stop\n"))
    if option==7:
        break
    elif option in (1,2,3,4,5,6):
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        if option==1:
            add(num1,num2)
        elif option==2:
            sub(num1,num2)
        elif option==3:
            mul(num1,num2)
        elif option==4:
            div(num1,num2)
        elif option==5:
            fldiv(num1,num2)
        elif option==6:
            exp(num1,num2)
    else:
        print("Invalid option")