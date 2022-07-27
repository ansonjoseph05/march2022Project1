# 4. create a function with argument to find factorial of a number given by user?

def factuser(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
n=int(input("Enter number to find factorial: "))
factuser(n)

