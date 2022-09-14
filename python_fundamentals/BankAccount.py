class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print(self.int_rate,self.balance)
        
    def yield_interest(self):
        self.balance-=self.balance * self.int_rate
        return self

karam=BankAccount(0.03,balance=3000)
ahmad=BankAccount(0.05,balance=10000)

karam.deposit(700).deposit(500).deposit(300).withdraw(1500).yield_interest().display_account_info()
ahmad.deposit(2700).deposit(1600).withdraw(900).withdraw(500).withdraw(700).withdraw(300).yield_interest().display_account_info()

