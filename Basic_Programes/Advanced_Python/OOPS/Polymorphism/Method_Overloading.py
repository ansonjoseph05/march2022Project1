# Polymorphism
# Contains two Methods
#1. Method Overloading
#2. Method Overriding

# overloading
# same method name diff num of arguments

class A:
    def printa(self,num1):
        self.num1=num1
        print(self.num1,"Inside A")
class B(A):
    def printb(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1,self.num2,"Inside B")

b=B()
b.printa(5)      # class A method
b.printa(5,8)    # class B method
