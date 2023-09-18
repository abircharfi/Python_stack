
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

guido = User("guido","guido8@gmail.com")
monty = User("monty","monty9@gmail.com")
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
monty.make_deposit(500)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50