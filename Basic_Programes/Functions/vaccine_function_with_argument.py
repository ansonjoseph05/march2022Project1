def vacc(name,age):
    if age>=18:
        print("Eligible")
    else:
        print("Not Eligible")
name=input("Enter name : ")
age=int(input("Enter age : "))
vacc(name,age)