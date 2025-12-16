class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("deposited:",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdraw:",amount)
        else:
            print("insufficent balance")
    def display(self):
        print("account holder name:",self.name)
        print("account no:",self.acc_no)
        print("balance:",self.balance)

acc=BankAccount("suresh",1234,5000)
acc.display()
acc.withdraw(1000)
acc.deposit(2000)
acc.display()
acc2=BankAccount("rajesh",1233,10000)
acc2.display()
acc2.withdraw(1000)
acc2.deposit(2000)
acc2.display()
