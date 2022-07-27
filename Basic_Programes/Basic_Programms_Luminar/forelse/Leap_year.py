n=int(input("Enter year: "))
if n%4==0 and n%100!=0 or n%400==0:
    print("Leap Year")
else:
    print("Not Leap Year")

    #leap year is the year having 1 day extra, ie 366 days
