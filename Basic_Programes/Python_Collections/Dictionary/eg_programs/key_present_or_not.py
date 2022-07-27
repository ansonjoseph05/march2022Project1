# check if a given key is present in a dictionary or not

d={'Anson':250,'Suresh':277,'Amal':380}
n=input("Enter key to be verified: ")
if n in d.keys():
    print("Key is present , Value is",d[n])
else:
    print("Key not present")
