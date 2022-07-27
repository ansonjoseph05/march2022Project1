class Person:
    def setvalue(self,name,age,place):           #we call the objects in class(name,age,place) as attributes
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
pe1=Person()
pe1.setvalue("Anu",18,"Kochi")
pe1.printvalue()

pe2=Person()
pe2.setvalue("Amal",21,"Calicut")
pe2.printvalue()
