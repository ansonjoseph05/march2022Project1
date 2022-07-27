# 2.create a function with argument and return type to find grade of student?

def stdgrade(n):
    if n < 49:
        return "F"
    elif 50<=n<=60:
        return "C"
    elif 61<=n<=70:
        return "B"
    elif 71<=n<=80:
        return "B+"
    elif 81<=n<=90:
        return "A"
    elif 91<=n<=100:
        return "A+"
    else:
        return "Invalid marks"
n1 = int(input("Enter Marks: "))
print(stdgrade(n1))
n2 = int(input("Enter Marks: "))
print(stdgrade(n2))
