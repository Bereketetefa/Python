class User:
    def __init__(self,name_param):
        self.name = name_param
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self, amount):
        self.account_balance = amount
        return self


oscar_obj = User("Oscar")
oscar_obj.make_deposit(5).make_deposit(5).make_deposit(5).make_withdrawal(5)
print(oscar_obj.account_balance)


myriam_obj= User("Myriam")
oscar_obj.make_deposit(10).make_deposit(10).make_withdrawal(5).make_withdrawal(5)
print(myriam_obj.account_balance)


dany_obj= User("dany")
dany_obj.make_deposit(100).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25)
print(dany_obj.account_balance)
