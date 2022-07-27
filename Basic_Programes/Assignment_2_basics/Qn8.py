# 8. print the pattern (Diamond)

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *


s=8
for i in range(7):
    for a in range(s):
        print(end=" ")
    s=s-1
    for j in range(i):
        print("*",end=" ")
    print()
s=3
for i in range(5,0,-1):
     for a in range(s):
         print(end=" ")
     s=s+1
     for j in range(i):
         print("*",end=" ")
     print()