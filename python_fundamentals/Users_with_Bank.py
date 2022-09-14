class BankAccount:
    def __init__(self,int_rate,account_balance):
        self.int_rate=int_rate
        self.balance=account_balance

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

class User:
    def __init__(self,name,email,int_rate,account_balance):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate,account_balance)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self,user,amount):
        user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self

karam=User("Karam Taha","karam@gmail.com",0.02,32000)
ahmad=User("Ahmad Taha","ahmad@gmail.com",0.04,13000)
malik=User("Malik Mohanna","malik@gmail.com",0.06,250000)

# karam.account = BankAccount(0.02, 32000)
# ahmad.account = BankAccount(0.04, 13000)
# malik.account = BankAccount(0.06, 250000)

karam.make_deposit(700).make_deposit(500).make_deposit(300).make_withdrawal(1500).yield_interest().display_user_balance()
ahmad.make_deposit(2700).make_deposit(1600).make_withdrawal(900).make_withdrawal(500).make_withdrawal(700).make_withdrawal(300).yield_interest().display_user_balance()
malik.make_deposit(3000).make_withdrawal(400).make_withdrawal(200).make_withdrawal(1700).yield_interest().display_user_balance()