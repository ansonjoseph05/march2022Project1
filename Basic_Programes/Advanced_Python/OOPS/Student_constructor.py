class Student:
    school="Luminar"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def printvalue(self):
        print(self.name,self.roll_no,Student.school)
name=input("Enter name: ")
st3=Student(name,16)
st3.printvalue()

st1=Student("Anson",11)
st1.printvalue()

st2=Student("Athul",12)
st2.printvalue()

print(st1.name)
print(st2.roll_no)
print(st1.school,st1.name)

