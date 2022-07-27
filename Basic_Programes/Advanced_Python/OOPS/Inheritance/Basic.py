# inheritance
# single inheritance

class A:                #parent class/super class/base class
    def printa(self):
        print("Inside A class")
class B(A):             #child class/sub class/derived class
    def printb(self):
        print("Inside B class")
b=B()
b.printb()
b.printa()




