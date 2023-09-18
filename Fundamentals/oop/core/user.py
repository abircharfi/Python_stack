from BankAccount import BankAccount


class user:

    number_accounts = []

    def __init__ (self, name, mail):

        self.name = name
        self.email = mail
        self.account = BankAccount(int_rate=0.02, balance=0)
        user.number_accounts.append(self)

    def deposit(self, amount):
        w=self.which_account(self.name)
        if w == True:
           self.account.deposit(amount)
           self.display_user_balance()
        elif w == False:
            print ("You should verify your account please")
        else :
            self.account.deposit(amount)
            print(f"User : {self.name}")
            self.display_user_balance() 
        return self

    def make_withdrawal(self, amount):
        w=self.which_account(self.name)
        if w == True:
           self.account.withdraw(amount)
           self.display_user_balance()
        elif w == False:
            print ("You should verify your account please")
        else :
            self.account.withdraw(amount)
            print(f"User : {self.name} {self.display_user_balance()}")
             

    def display_user_balance(self):
        self.account.display_account_info()
        
        return self
    
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self
    
    @classmethod
    def which_account(cls,name):
        number=0
        for i in range (len(cls.number_accounts)):
            if name == cls.number_accounts[i].name:
             number+=1
             if number > 1:
              print (f"you have {number} accounts which one you mean" )
              mail = input("write your email : ")
              
              res= cls.which_mail(mail,name)
              if res == True:
                  print(f"User: {name} your account {mail}")
                  return True
              else:
                 return False
             
              
    @classmethod
    def which_mail(cls,mail,name):
       dict ={}
       for i in range (len(cls.number_accounts)):
             dict[cls.number_accounts[i].email] = cls.number_accounts[i].name 
       for key, value in dict.items():
           if mail == key and name == value:
              return True 
       return False
       
                      

glori=user("glori","glori@live.fr")
glori=user("glori","glori@google.com")

glori.deposit(100)
glori.make_withdrawal(20)

aline=user("Aline", "aline5@gmail.com")
aline.deposit(80)
