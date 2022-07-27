# queue       FIFO (First in first out)
# list
# add element     enqueue
# remove element    dequeue
# display



queue=[]
size=int(input("Enter the size"))
top=0
def enqueue():
    global top,size
    if top>=size:
        print("queue is full")
    else:
        e=int(input("Enter element to add"))
        queue.append(e)
        top=top+1
        print(queue)
def dequeue():
    global top,size
    if top<=0:
        print("Queue is empty")
    else:
        queue.remove(queue[0])                   # here the difference between stack is that in queue the removal is first in first out
        top=top-1                                # so we remove the first element in the queue, rest is same
        print(queue)
while True:
    option=int(input("Enter operation\n1.enqueue\n2.dequeue\n"))
    if option==1:
        enqueue()
    else:
        dequeue()

