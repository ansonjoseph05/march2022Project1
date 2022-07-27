# **kwargs - keyword arguments
def printdata(**kwargs):
    print(kwargs)
printdata(name="Anson",age=22,place="Kottayam")


# here **kwargs will always be dictionary , and the name of dictionary is kwarg here
# also we can name any variable after **, but ** is must
