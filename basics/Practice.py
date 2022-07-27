#marks and grade

mark=float(input("Enter Total Marks Percentage :"))
if mark>90 and mark<=100:
    print("A")
elif mark>=80 and mark<=89:
     print("B")
elif mark>=70 and mark<=79:
    print("C")
elif mark>=60 and mark<=69:
    print("D")
elif mark>=50 and mark<=59:
    print("E")
elif mark>100:
    print("Invalid Marks")
if mark<=50:
    print("Failed")





