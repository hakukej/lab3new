class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount
        print(f"balance: {self.balance}")
    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
            print(f"balance: {self.balance}")
        else:
            print("Balance is not enough")
a = Bank("Akerke", 500)
a.deposit(200)
a.withdraw(500)
a.withdraw(300)