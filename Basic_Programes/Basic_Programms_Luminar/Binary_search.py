l=[1,2,3,4,5,6,7,8,9]
e=int(input("Enter element to search"))
l.sort()        #[1,2,3,4,5,6,7,8,9]
flag=0                                     # no need to study binary search but understand and learn the operations used
low=0
upper=len(l)-1
while low<=upper:
    mid=(low+upper)//2   #mid=7
    if l[mid]==e:
        flag=1
        break
    elif e>l[mid]:
        low=mid+1        #low=6
    elif e<l[mid]:
        upper=mid-1
if flag==1:
    print("Found")
else:
    print("Not Found")
    
