class BankAccount:
	def __init__(self, int_rate, balance): 
        self.intrest = int_rate
        self.balance = balance 

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
        if self.balance >= amount:
		    self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

	def display_account_info(self):
        print(f"balance ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance = (self.balance * self.intrest)
        return self


bankaccount1 = BankAccount(0.05)
bankaccount2 = BankAccount(0.5, 100)

bankaccount1.deposit(100).yield_interest().display_account_info()

