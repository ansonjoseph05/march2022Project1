# 5. Python program to find the sum of prime numbers in an interval

initial=int(input("Enter initial value: "))
final=int(input("Enter final value: "))
sum=0
for i in range(initial,final+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum+=i
print(sum)