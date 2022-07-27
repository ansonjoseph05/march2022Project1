# multilevel/hierarchial

# here class A is Parent class
# Class B is both Parent and child class
# and class C is child class

class A:
    def printa(self):
        print("Inside A")
class B(A):
    def printb(self):
        print("Inside B")
class C(B):
    def printc(self):
        print("Inside C")
c=C()
c.printa()
c.printb()
c.printc()
