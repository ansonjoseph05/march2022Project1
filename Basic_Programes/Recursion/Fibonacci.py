fdef recfib(n):
    if n<=1:                              #imp qn
        return n
    else:
        return recfib(n-1)+recfib(n-2)
nterms=int(input("Enter number of terms: "))
for i in range(nterms):    # i=0,1,2,3,4,5,....
    print(recfib(i))
#recfib(0)=0
#recfib(1)=1
#recfib(2)=1
#recfib(3)=2