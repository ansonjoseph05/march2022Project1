# tostring  (__str__)

class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
    def __str__(self):                                          #     {      to string
        return self.name+self.place+str(self.age)               #                 method              }
pe1=Person()
pe1.setvalue("Anu",18,"Kochi")
print(pe1)