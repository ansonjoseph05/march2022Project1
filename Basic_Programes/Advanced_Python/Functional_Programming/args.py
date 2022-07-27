# *args
# def printnumbers(*args):
#     print(args)
# printnumbers(1,8,4,2,5,6)

# here *args will always be tuple , and the name of tuple is arg here
# also we can name any variable after *, but * is must


# sum of  numbers
def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
sum(1,2,3)
sum(1,2,3,4,5)
