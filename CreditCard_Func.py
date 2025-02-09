class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def check_balance(self):
        return self.balance
    
    def withdraw(self, amt):
        if amt < amt:
            print("Insufficient funds")
        else: 
            self.balance -= amt