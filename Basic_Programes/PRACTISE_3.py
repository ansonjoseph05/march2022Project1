n=int(input("Enter student marks: "))
if n < 49:
    print("F")
elif 50 <= n <= 60:
    print("C")
elif 61 <= n <= 70:
    print("B")
elif 71 <= n <= 80:
    print("B+")
elif 81 <= n <= 90:
    print("A")
elif 91 <= n <= 100:
    print("A+")
else:
    print("Invalid marks")
