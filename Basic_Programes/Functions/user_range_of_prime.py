initial=int(input("Enter initial value :")) #1
final=int(input("Enter final value :"))   #5
for i in range(initial,final+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

