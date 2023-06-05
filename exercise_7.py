#Bank account

class BankAccount:
    def __init__(self):
        self.cash = 0
    
    def depositing(self, amount):
        self.cash = self.cash + abs(amount)
    
    def withdrawing(self, amount):
        self.cash = self.cash - abs(amount)
    
    def check(self):
        print(f'The account balance is {self.cash}')


account = BankAccount()
