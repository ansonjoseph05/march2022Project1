# data structures


#1. stack    (Last in first out(LIFO))
# size
# add element... push operation... to do push operation we have to ensure stack is not full
# remove element... pop operation... to do pop operation we have to ensure stack is not empty (pop operation removes the last element)
# display
# we can use list to do stack since pop is present in list

stack=[]
size=int(input("Enter the size"))
top=0
def push():
    global top,size
    if top>=size:
        print("Stack is full")
    else:
        e=int(input("Enter element to add"))
        stack.append(e)
        top=top+1
        print(stack)
def pop():
    global top,size
    if top<=0:
        print("Stack is empty")
    else:
        stack.pop()
        top=top-1
        print(stack)
while True:
    option=int(input("Enter operation\n1.push\n2.pop\n"))
    if option==1:
        push()
    else:
        pop()


