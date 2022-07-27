class Employee:
    def setvalue(self,name,id,designation,company):
        self.name=name
        self.id=id
        self.designation=designation
        self.company=company
    def printvalue(self):
        print(self.name)
        print(self.id)
        print(self.designation)
        print(self.company)
em1=Employee()
em1.setvalue("Anson",2332,"Junior Software Developer","TCS")
em1.printvalue()

em2=Employee()
em2.setvalue("Athul",287784,"Junior Software Developer","TCS")
em2.printvalue()