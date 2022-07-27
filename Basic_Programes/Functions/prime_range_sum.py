initial=int(input("Enter initial value : ")) #1
final=int(input("Enter final value : ")) #5
sum=0
for i in range(initial,final+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum=sum+i
print(sum)

