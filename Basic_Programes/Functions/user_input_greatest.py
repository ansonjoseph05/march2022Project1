def great(n1,n2):
    if n1>n2:
        return n1
    elif n1==n2:
        return "Equal"
    else:
        return n2
n1=int(input("Enter a number : "))
n2=int(input("Enter a number : "))
print(great(n1,n2))
