mark=int(input("Enter Marks :"))      #nestedif case
if mark>100:
    print("Invalid Marks")
elif mark>=90:
    print("A+")
elif mark>=80:
    print("A")
elif mark>=70:
    print("B+")
elif mark>=60:
    print("C")
elif mark>=45:
    print("D")
elif mark<45:
    print("Failed")

