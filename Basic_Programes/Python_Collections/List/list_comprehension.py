#list comprehension
#
# l=[1,2,5,7,9]
# square=[]
# for i in l:
#     square.append(i*i)
# print(square)




# l=[1,2,5,7,9]
# square=[i*i for i in l]
# print(square)



# listn=[i for i in range(1,11)]
# print(listn)


#positive and negative

# l=[1,-3,5,-7,-1,4,7,9]
# listn=[i for i in l if i<0 ]
# print("Positive",listn)
# listn1=[i for i in l if i>0]
# print("Negative",listn1)


#range 20 even

even=[i for i in range(0,21) if i%2==0]
print(even)