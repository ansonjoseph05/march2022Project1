class Student:
    def setvalue(self,name,roll_no,department):
        self.name=name
        self.roll_no=roll_no
        self.department=department
    def printvalue(self):
        print(self.name)
        print(self.roll_no)
        print(self.department)
st1=Student()
st1.setvalue("Anson",12,"ECE")
st1.printvalue()

st2=Student()
st2.setvalue("Athul",13,"CSEa")
st2.printvalue()

st3=Student()
st3.setvalue("Gokul",15,"CSE")
st3.printvalue()

