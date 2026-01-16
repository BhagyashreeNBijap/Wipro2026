'''#Topics: Parameterized Methods, Constructors & Destructors
Create a class BankAccount that:
1. Uses a parameterized constructor to initialize account_number and balance
2. Implements methods deposit(amount) and withdraw(amount)
3. Uses a destructor to display a message when the object is deleted
4. Handle invalid withdrawal using proper checks'''


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Account created successfully")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
            print(f"Current Balance: ₹{self.balance}")

    def __del__(self):
        print(f"Account {self.account_number} is closed")

account = BankAccount(123456, 5000)

account.deposit(2000)
account.withdraw(3000)
account.withdraw(10000)

del account
