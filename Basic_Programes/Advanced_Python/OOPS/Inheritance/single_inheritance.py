# here Person and Parent are Parent Class and Employee is child class


class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def setstudent(self,roll,dept,school):
        self.roll=roll
        self.dept=dept
        self.school=school
    def printvalue(self):
        print(self.name,self.age,self.place,self.roll,self.dept,self.school)
st=Student()
st.setvalue("Anson",22,"Kottayam")
st.setstudent(12,"ECE","Luminar")
st.printvalue()