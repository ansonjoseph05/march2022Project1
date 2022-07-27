# raise exception

age=int(input("Enter age: "))
if age<18:
    raise Exception("Not eligible")
else:
    print("Eligible")
