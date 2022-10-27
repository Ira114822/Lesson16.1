class BankAccount:
    pass

    def __int__(self):
        print("constructor from BankAccount")

    def __del__(self):
        print("destructor from BankAccount")

account1 = BankAccount()

BankAccount.__int__(account1)

account1.name = "12345"
account1.balance = 1_000_000

account2 = BankAccount()
account2.name = "67890"
account2.balance = 1_000