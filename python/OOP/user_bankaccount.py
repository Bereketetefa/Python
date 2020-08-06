class BankAccount:
	def __init__(self,int_rate,balance):
        self.interest = int_rate
        self.balance = balance

	def deposit(self, amount):
		self.balance += amount
        return self

	def withdraw(self, amount):
        if self.balance >= amount:
		    self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

	def display_accountInfo(self):
        print(f"balance ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.interest)
        return self



class User:
    def __init__(self,username,email_address):
        self.name = username
        self.name = email_address
        self.checking = BankAccount(0,0)
        # self.savings = BankAccount(0.01, 0)

    def make_deposit(self, amount):
        # self.account_balance += amount
        self.checking.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        # self.account_balance -= amount
        self.checking.withdraw(amount)
        return self

    def display_balance(self, amount):
        print (f"User Name: {self.name}. Account balance: {self.checking.balance}")
        return self

    def transfer_money(self, otheruser, amount):
        self.account_balance -= amount
        otheruser.account_balance += amount
        return self


oscar_obj = User("Oscar")
myriam_obj= User("Myriam")
dany_obj= User("dany")
oscar_obj.make_deposit(100).display_balance






# bankaccount1 = user("bankaccount1")
# bankaccount1 = BankAccount(0.05)
# bankaccount2 = BankAccount(0.5, 100)

# bankaccount1.deposit(100).yield_interest().display_account_info()

