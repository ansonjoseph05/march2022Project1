# Exception Handling

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
try:
    print("in try")
    print(num1 / num2)
except Exception as error:
    print(error)
finally:
    print("in finally")


#
# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))
# try:
#     print("in try")                   #try block always works,
#     print(num1/num2)
# except:                               #except block works only when error or exception occurs
#     print("error occured")
# finally:                              #finally block always works  (normally finally is not used in web development)
#     print("in finally")
#
                                      #the main purpose of error handling is to clear the red error in the compiler