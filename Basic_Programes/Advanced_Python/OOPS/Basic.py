#object oriented programming

# Basic Terms
# 1. class - design pattern/blueprint  ,class is a collection of methods and variables
# 2. object - real-world entity
# 3. reference - store and perform operations

#eg:
class Person:
    def walk(self):
        print("Person is walking")
    def read(self):
        print("Person is readig")
pe1=Person()
pe1.walk()
pe1.read()

pe2=Person()
pe2.read()
pe2.walk()