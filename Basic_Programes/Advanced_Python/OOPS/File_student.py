class Student:
    def __init__(self,name,roll_no,mark):
        self.name=name
        self.roll_no=roll_no
        self.mark=mark
    def printpa(self):
        print(self.name, self.roll_no,self.mark)
f = open('student.txt', 'r')
for i in f:
    data = i.rstrip("\n").split(",")
    # print(data)
    name = data[0]
    roll_no = data[1]
    mark = data[2]
    st = Student(name, roll_no,mark)
    st.printpa()