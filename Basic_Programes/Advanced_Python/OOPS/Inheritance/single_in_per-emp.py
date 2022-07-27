# here Person and Parent are Parent Class and Employee is child class


class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
class Employee(Person):
    def setemployee(self,id,desig,company):
        self.id=id
        self.desig=desig
        self.company=company
    def printvalue(self):
        print(self.name,self.age,self.place,self.id,self.desig,self.company)
st=Employee()
st.setvalue("Anson",22,"Kottayam")
st.setemployee(1234,"Jr Software Engineer","TCS")
st.printvalue()