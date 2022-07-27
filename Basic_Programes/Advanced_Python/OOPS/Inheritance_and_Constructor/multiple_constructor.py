class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Parent:
    def __init__(self,phone,address):
        self.phone=phone
        self.address=address
    def printparent(self):
        print(self.phone,self.address)
class Employee(Person,Parent):
    def __init__(self,id,desig,company,name,age,place,phone,address):
        Person.__init__(self,name,age,place)
        Parent.__init__(self,phone,address)
        self.id=id
        self.desig=desig
        self.company=company
    def printemployee(self):
        print(self.id,self.desig,self.company)
emp=Employee(1,"Jr Software Developer","Infopark","Anson",22,"Kottayam","abc","445678999")
emp.printemployee()
emp.printperson()
emp.printparent()