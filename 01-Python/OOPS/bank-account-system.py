from abc import ABC, abstractmethod

# ---------------- ABSTRACTION ----------------
class Account(ABC):

    # Class Variables
    bank_name = "City Bank"
    total_accounts = 0

    # Constructor
    def __init__(self, acc_holder, acc_no, balance):
        self.acc_holder = acc_holder
        self.acc_no = acc_no
        self.__balance = balance      # Private Variable (Encapsulation)

        Account.total_accounts += 1

    # ---------------- ENCAPSULATION ----------------
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} Deposited Successfully.")
        else:
            print("Invalid Deposit Amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Withdraw Amount.")
        elif amount > self.__balance:
            print("Insufficient Balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} Withdrawn Successfully.")

    # ---------------- ABSTRACTION ----------------
    @abstractmethod
    def calculate_interest(self):
        pass

    def show_details(self):
        print(f"Account Number : {self.acc_no}")
        print(f"Holder Name    : {self.acc_holder}")
        print(f"Bank Name      : {Account.bank_name}")
        print(f"Balance        : ₹{self.get_balance()}")


# ---------------- INHERITANCE ----------------
class SavingsAccount(Account):

    def __init__(self, acc_holder, acc_no, balance, rate):
        super().__init__(acc_holder, acc_no, balance)
        self.rate = rate
        self.account_type = "Savings Account"

    # ---------------- METHOD OVERRIDING ----------------
    def calculate_interest(self):
        return self.get_balance() * self.rate / 100

    def show_details(self):
        super().show_details()
        print(f"Account Type   : {self.account_type}")
        print(f"Interest       : ₹{self.calculate_interest()}")


class CurrentAccount(Account):

    def __init__(self, acc_holder, acc_no, balance, overdraft_limit):
        super().__init__(acc_holder, acc_no, balance)
        self.overdraft_limit = overdraft_limit
        self.account_type = "Current Account"

    # ---------------- METHOD OVERRIDING ----------------
    def calculate_interest(self):
        return 0

    def show_details(self):
        super().show_details()
        print(f"Account Type   : {self.account_type}")
        print(f"Overdraft      : ₹{self.overdraft_limit}")
        print(f"Interest       : ₹{self.calculate_interest()}")


# ---------------- MULTILEVEL INHERITANCE ----------------
class FixedDeposit(SavingsAccount):

    def __init__(self, acc_holder, acc_no, balance, rate, tenure):
        super().__init__(acc_holder, acc_no, balance, rate)
        self.tenure = tenure
        self.account_type = "Fixed Deposit"

    # ---------------- METHOD OVERRIDING ----------------
    def calculate_interest(self):
        return super().calculate_interest() * self.tenure

    def show_details(self):
        super().show_details()
        print(f"Tenure         : {self.tenure} Years")
        print(f"Total Interest : ₹{self.calculate_interest()}")


# ---------------- MAIN PROGRAM ----------------

acc1 = SavingsAccount("Arun", "SB101", 50000, 4)
acc2 = CurrentAccount("Divya", "CA202", 75000, 20000)
acc3 = FixedDeposit("Karthik", "FD303", 100000, 6, 3)

accounts = [acc1, acc2, acc3]

acc1.deposit(5000)
acc2.withdraw(10000)

print("\nACCOUNT DETAILS\n")

for account in accounts:
    print("-" * 40)
    account.show_details()

print("-" * 40)
