num=int(input("Enter a number :"))
initial=int(input("Enter initial value :"))
final=int(input("Enter final value :"))
for i in range(initial,final+1):
    print(i,"*",num,"=",i*num)