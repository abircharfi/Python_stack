class BankAccount:

    balance =0
    all_accounts = []
    
    def __init__(self, int_rate, balance): 
        
        self.interest_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $"+amount+ "fee and deduct $"+amount)
        
    def display_account_info(self):
        print(f"Balance : $ {self.balance}")
        return self

    def yield_interest(self):
        if (self.balance)>0:
            self.balance += self.balance * self.interest_rate
        return self
    def can_withdraw(balance,amount):
    	if (balance - amount) > 0:
            return True


    @classmethod
    def all_instances(cls):
        for i in range (len(cls.all_accounts)):
            cls.all_accounts[i].display_account_info()
    @classmethod
    def whitch_acc(cls):
        for i in range (len(cls.all_accounts)):
           print(cls.all_accounts[i])
            
    
    

#first_account=BankAccount(0.1,500).deposit(600).deposit(50).deposit(95).withdraw(100).yield_interest().display_account_info()
#second_account=BankAccount(0.01,50).deposit(600).deposit(95).withdraw(10).withdraw(10).yield_interest().display_account_info()

BankAccount.all_instances()

