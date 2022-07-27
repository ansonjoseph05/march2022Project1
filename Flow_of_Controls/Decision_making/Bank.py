print("Account Balance = 100000")
amount=int(input("Enter the amount to be withdrawn :"))
Tamount=100000
print("Balance",Tamount-amount)
if amount>Tamount:
    print("Insufficient Balance")
else:
    print("Successful Transaction")

