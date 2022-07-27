initial=int(input("Enter a number :"))
final=int(input("Enter a number :"))
sum=0
for i in range(initial,final+1):
    if i>0:
        sum+=i
print(sum)