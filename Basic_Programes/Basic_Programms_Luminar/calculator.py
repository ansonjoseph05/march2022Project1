# calculator
# select operations
# add
# sub
# mul
# div
# stop
# 1     num1 num2    sum
# 2       num1 num2   subres
# 7   invalid

def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mul(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)
while True:
    option=int(input("select options\n1.add\n2.sub\n3.mul\n4.div\n5.stop"))
    if option==5:
        break
    elif option in (1,2,3,4):
        num1=float(input("Enter num1: "))
        num2=float(input("Enter num2: "))
        if option==1:
            add(num1,num2)
        elif option==2:
            sub(num1,num2)
        elif option==3:
            mul(num1,num2)
        else:
            div(num1,num2)
    else:
        print("Invalid option")