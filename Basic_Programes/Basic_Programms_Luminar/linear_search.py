l=[1,2,3,4,5,6,7]
def linear(e):
    for i in l:
        if i==e:
            print("Present")
            break
    else:
        print("Not present")
e=int(input("Enter number to search: "))
linear(e)