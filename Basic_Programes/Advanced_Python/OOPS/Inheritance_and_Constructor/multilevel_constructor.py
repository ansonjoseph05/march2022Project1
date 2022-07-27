class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Parent(Person):
    def __init__(self,phone,address,name,age,place):
        super().__init__(name,age,place)
        self.phone=phone
        self.address=address
    def printparent(self):
        print(self.phone,self.address)
class Employee(Parent):
    def __init__(self,name,age,place,phone,address,id,desig,company):
        super().__init__(name,age,place,phone,address)
        self.id=id
        self.desig=desig
        self.company=company
    def printemployee(self):
        print(self.id,self.desig,self.company)
emp=Employee("Anson",22,"Kottayam",87578990,"hgh",78768,"Jr software engineer","Infopark")
emp.printemployee()
emp.printparent()
emp.printperson()