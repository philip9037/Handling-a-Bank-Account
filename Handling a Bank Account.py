class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return self.balance * self.interestRate / 100
acc = Account("John Doe", 2000)
acc.deposit(500)
print(acc.getBalance())  
acc.withdrawal(700)
print(acc.getBalance())  

savings_acc = SavingsAccount("Jane Doe", 2000, 5)
print(savings_acc.interestAmount())  
