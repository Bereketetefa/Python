class User:
    def __init__(self,name_param):
        self.name = name_param
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self, amount):
        self.account_balance = amount
    

#  Have the first user make 3 deposits and 1 withdrawal and then display their balance

oscar_obj = User("Oscar")
oscar_obj.make_deposit(5)
oscar_obj.make_deposit(5)
oscar_obj.make_deposit(5)
print(oscar_obj.account_balance)

oscar_obj.make_withdrawal(5)
print(oscar_obj.account_balance)

#  Have the second user make 2 deposits and 2 withdrawals and then display their balance

myriam_obj= User("Myriam")
myriam_obj.make_deposit(10)
myriam_obj.make_deposit(10)
print(myriam_obj.account_balance)

myriam_obj.make_withdrawal(5)
myriam_obj.make_withdrawal(5)
print(myriam_obj.account_balance)

#  Have the third user make 1 deposits and 3 withdrawals and then display their balance

dany_obj= User("dany")
dany_obj.make_deposit(100)
print(dany_obj.account_balance)

dany_obj.make_withdrawal(25)
dany_obj.make_withdrawal(25)
dany_obj.make_withdrawal(25)
print(dany_obj.account_balance)

