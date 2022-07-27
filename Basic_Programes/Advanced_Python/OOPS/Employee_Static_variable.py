# #Static variable
#
# # self is used to point to the current instance
# # instance variable ... related to methods... self
# # static variable ... related to class... class name
#
#
class Employee:
    designation="Junior Software Developer"                   #static variable
    company="TCS"                                             #static variable
    def setvalue(self,name,id):
        self.name=name                                        #instance variable
        self.id=id                                            #instance variable
    def printvalue(self):
        print(self.name,self.id,Employee.designation,Employee.company)
em1=Employee()
em1.setvalue("Anson",2332)
em1.printvalue()

em2=Employee()
em2.setvalue("Athul",287784)
em2.printvalue()



