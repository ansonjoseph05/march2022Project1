# multiple inheritance

class A:
    def printa(self):
        print("inside A")
class B:
    def printb(self):
        print("inside B")
class C(A,B):
    def printc(self):
        print("insie C")
c=C()
c.printc()
c.printa()
c.printb()
