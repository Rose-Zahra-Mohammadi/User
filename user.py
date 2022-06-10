# declare a class and give it name User


class User:
# declaring a class attribute
    bank_name = "First National Dojo"		
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: $" + str(self.account_balance))
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

guido = User("Gudio van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rose = User("Rose Moha", "rose@python.com")
# Accessing the instance's attributes
# print(guido.name)  # output: Michael
# print(monty.name)  # output: Michael
monty.make_deposit(20)
guido.make_deposit(10)
rose.make_deposit(200)
monty.display_user_balance()
rose.transfer_money(monty, 15).display_user_balance()