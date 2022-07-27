class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def __init__(self,roll,dept,school,name,age,place):
        super().__init__(name,age,place)
        self.roll=roll
        self.dept=dept
        self.school=school
    def printstudent(self):
        print(self.name,self.age,self.place,self.roll,self.dept,self.school)
st=Student(1,"CSE","Luminar","Anson",22,"Kottayam")
st.printstudent()
st.printvalue()