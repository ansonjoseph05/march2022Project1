d1={1:"a",2:"b",3:"c"}
d2={4:"d",5:"e",6:"f"}
#print(d)
#print(d.keys())                       # prints keys
#print(d.values())                     # prints values
d1.update(d2)                          # concatenate dictionaries (joins dictionaries)
print(d1)