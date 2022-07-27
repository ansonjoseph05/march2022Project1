#3. create a function to find sum of odd numbers from 20 to 30?

def oddsum(n1,n2):
    sum=0
    for i in range(n1,n2+1):
        if i%2!=0:
            sum+=i
    print(sum)
oddsum(20,30)
