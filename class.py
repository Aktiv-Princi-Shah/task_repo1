class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount)
        else:
            print("Not enough balance!!")

    def show_balance(self):
        print("Balance for", self.account_holder, ":", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print("Interest added:", interest)

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrew:", amount)
        else:
            print("Overdraft limit reached!")

def main():
    acc_type = input("Enter account type enter 1 for savings and 2 for current: ")
    acc_no = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    if acc_type == "1":
        rate = float(input("Enter interest rate value like 0.05 for 5%: "))
        account = SavingsAccount(acc_no, name, balance, rate)
    elif acc_type == "2":
        limit = float(input("Enter overdraft limit: "))
        account = CurrentAccount(acc_no, name, balance, limit)
    else:
        print("Invalid account type.")
        return

    while True:
        print("\nOptions Menu\n 1. deposit\n 2. withdraw\n 3. balance\n 4. interest\n 5. exit\n")
        choice = input("Choose an action: ").lower()
        if choice == "1":
            amt = int(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == "2":
            amt = int(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            if isinstance(account, SavingsAccount):
                account.add_interest()
            else:
                print("Interest only applies to savings account!!")
        elif choice == "5":
            print("Exit!!")
            break
        else:
            print("Invalid choice!")
main()

