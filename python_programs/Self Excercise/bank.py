# Create a bank account class having two attributes:
# Account holder and Balance and two methods: 
# Deposits and Withdraw. Make some deposit and withdraw
# but withdraw amount cannot exceed the available balance.

class Account:
    def __init__(self, account_holder, balance):
        self.available_balance = balance
        #self.balance = balance
        self.account_holder = account_holder
    
    def __str__(self):
        return f"Account holder name: {self.account_holder} \nAvailable Balanece: {self.available_balance}\n"
    
    def Deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.available_balance = self.available_balance + self.deposit_amount
        #return self.deposit_amount
        print(f"{self.deposit_amount} is added in {self.account_holder}'s account, total avaialbe balance is {self.available_balance}.\n")
    
    def Withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.available_balance < self.withdraw_amount:
            print("Insufficient balance")
        else:
            self.available_balance = self.available_balance - self.withdraw_amount
            #self.balance = self.balance + self.withdraw_amount
            #return self.available_balance
            print(f"{self.withdraw_amount} is withdrawn from {self.account_holder}'s account, total available balance is {self.available_balance}.")

object = Account("Sam", 1000)
print(object)
object.Deposit(100)
object.Withdraw(1000)
