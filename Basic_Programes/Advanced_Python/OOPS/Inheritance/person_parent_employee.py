class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Parent:
    def setparent(self,phone,address):
        self.phone=phone
        self.address=address
    def printparent(self):
        print(self.phone,self.address)
class Employee(Person,Parent):
    def setemployee(self,id,desig,company):
        self.id=id
        self.desig=desig
        self.company=company
    def printemployee(self):
        print(self.id,self.desig,self.company)
em=Employee()
em.setperson("Anson",22,"Kottayam")
em.printperson()
em.setparent(9497576380,"Kunnumpuram")
em.printparent()
em.setemployee(1234,"Jr Software Developer","TCS")
em.printemployee()


