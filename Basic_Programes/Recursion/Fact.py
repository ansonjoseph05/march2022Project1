def recfact(n):
    if n==1:
        return n                        #Note : we can only use return in recursion
    else:
        return n*recfact(n-1)
print(recfact(4))