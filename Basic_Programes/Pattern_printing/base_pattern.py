#basics

#print("*",end="")        #end="" stops the control to go to the next row
#print("*",end="")
#print("*",end="")
#print()
#for i in range(5):
#    print(i,end="")



#first pattern (*)
#
# for i in range(5):        #i=2
#   for j in range(i):    #j=0,1,2
#        print("*",end=" ")
#   print()

# *
# * *
# * * *
# * * * *

     #or


# for i in range(5):                    (This code is applicable for this program only)
#     print("* "*i)


#reverse pattern (*)
#
# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# * * * *
# * * *
# * *
# *


#pattern (int)

# num=0
# for i in range(5):
#     for j in range(i):
#         num=num+1
#         print(num,end=" ")
#     print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10


#pattern (int)(i+j)

# for i in range(5):
#     for j in range(i):
#         print(i+j,end=" ")
#     print()


# 1
# 2 3
# 3 4 5
# 4 5 6 7

#pattern (int)

# for i in range(5):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4

#pattern (int)

# for i in range(5):
#     for j in range(i):
#         print(j,end=" ")
#     print()

# 0
# 0 1
# 0 1 2
# 0 1 2 3


#multiplication table(i*j)

# for i in range(5):
#     for j in range(i):
#         print(i*j,end=" ")
#     print()

# 0
# 0 2
# 0 3 6
# 0 4 8 12

#pattern (int(i-j))

# for i in range(5):
#     for j in range(i):
#         print(i-j,end=" ")
#     print()

# 1
# 2 1
# 3 2 1
# 4 3 2 1

#pattern (int)(j-i)

# for i in range(5):
#     for j in range(i):
#         print(j-i,end=" ")
#     print()

# -1
# -2 -1
# -3 -2 -1
# -4 -3 -2 -1

#rectangle pattern

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()


#pyramid pattern
#
# s=6
# for i in range(5):
#     for a in range(s):
#         print(end=" ")
#     s=s-1
#     for j in range(i):
#         print("*",end=" ")
#     print()


#paralellogram pattern

# s=1
# for i in range(5):
#     for a in range(s):
#         print(end=" ")
#     s=s+1
#     for j in range(5):
#         print("*",end=" ")
#     print()

#         OR

# for i in range(5):
#     for a in range(i):
#         print(end=" ")
#     for j in range(5):
#         print("*",end=" ")
#     print()


#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *
#      * * * * *

#paralellogram pattern(opposite shape)

# s=6
# for i in range(5):
#     for a in range(s):
#         print(end=" ")
#     s=s-1
#     for j in range(5):
#         print("*",end=" ")
#     print()


#      * * * * *
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *


#inverted pyramid

# s=1
# for i in range(5,0,-1):
#     for a in range(s):
#         print(end=" ")
#     s=s+1
#     for j in range(i):
#         print("*",end=" ")
#     print()
#

#  * * * *
#   * * *
#    * *
#     *

