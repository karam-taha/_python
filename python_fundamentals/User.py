class User:
    def __init__(self,name,email,account_balance):
        self.name=name
        self.email=email
        self.account_balance=account_balance

    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name,self.account_balance)

    def transfer_money(self,user,amount):
        user.make_deposit(amount)
        self.make_withdrawal(amount)
        
karam=User("Karam Taha","karam@gmail.com",account_balance=3000)
ahmad=User("Ahmad Taha","ahmad@gmail.com",account_balance=10000)
malik=User("Malik Mohanna","malik@gmail.com",account_balance=20000)

karam.make_deposit(100)
karam.make_deposit(500)
karam.make_deposit(300)
karam.make_withdrawal(1500)
karam.transfer_money(malik,300)
karam.display_user_balance()

ahmad.make_deposit(1000)
ahmad.make_deposit(700)
ahmad.make_withdrawal(300)
ahmad.make_withdrawal(1500)
ahmad.display_user_balance()

malik.make_deposit(3000)
malik.make_withdrawal(400)
malik.make_withdrawal(200)
malik.make_withdrawal(1700)
malik.display_user_balance()

# print(karam.account_balance)
# print(ahmad.account_balance)
# print(malik.account_balance)

