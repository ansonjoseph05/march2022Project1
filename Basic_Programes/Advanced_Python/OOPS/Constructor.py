# Constructor

#  constructor is used to initialse instance variable at the time of creating objects.

class Add:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printsum(self):
        print(self.num1+self.num2)
add1=Add(100,200)
add1.printsum()

