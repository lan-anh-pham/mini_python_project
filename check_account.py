class Account():
    def __init__(self,owner,balance):
        self.owner= owner
        self.balance= balance
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    def deposit(self,amount_in):
        self.balance += amount_in
        print("Deposit Accepted")
    def withdrawal(self, amount_out):
        if amount_out <= self.balance:
            self.balance -= amount_out
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable")

myaccount= Account("Leah",500)
print(myaccount)

hisaccount= Account("Hoang",200)
print(hisaccount)


print(isinstance(myaccount,Account))
