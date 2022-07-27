# Method Overriding

# when same method name and same number of arguments, child class method overrides parent class method

class A:
    def printa(self,num1):
        self.num1=num1
        print(self.num1,"Inside A")
class B(A):
    def printa(self,no1):
        self.no1=no1
        print(self.no1,"Inside B")
b=B()
b.printa(6)




