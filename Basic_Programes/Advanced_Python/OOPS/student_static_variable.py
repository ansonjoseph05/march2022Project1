class Student:
    department="CSE"                       #Static variable
    def setvalue(self,name,roll_no):
        self.name=name                     #instance variable
        self.roll_no=roll_no               #instance variable

    def printvalue(self):
        print("Student name is",self.name)
        print("Roll no: is",self.roll_no)
        print("Department is",Student.department)

st1=Student()
st1.setvalue("Anson",12)
st1.printvalue()

st2=Student()
st2.setvalue("Athul",13)
st2.printvalue()

st3=Student()
st3.setvalue("Gokul",15)
st3.printvalue()

