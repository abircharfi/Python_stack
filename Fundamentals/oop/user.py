class user:

    def __init__ (self, name, mail):

        self.name = name
        self.email = mail
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print ("User : "+ self.name + ", Balance : $" + str(self.account_balance) )
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

glori=user("glori","glori@live.fr")
safa=user("safa","safa@live.fr")
aline=user("Aline", "aline5@gmail.com")

glori.deposit(100).deposit(200).deposit(500).make_withdrawal(150).display_user_balance()

safa.deposit(500).deposit(50).make_withdrawal(250).make_withdrawal(80).display_user_balance()

aline.deposit(1000).make_withdrawal(250).make_withdrawal(180).make_withdrawal(75).display_user_balance()

glori.transfer_money(aline,50).display_user_balance()
aline.display_user_balance()

