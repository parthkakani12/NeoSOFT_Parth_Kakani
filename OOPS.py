# Bank Account Management System using OOP


class MinimumBalanceError(Exception):
    pass


class OverdraftExceededError(Exception):
    pass


class Account:

    def __init__(self, holder_name, opening_balance):
        self.__holder_name = holder_name
        self.__balance = opening_balance
        self.__history = [("Account Opened", opening_balance)]

    def deposit(self, amount):
        self.__balance += amount
        self.__history.append(("Deposit", amount))

    def withdraw(self, amount):
        self.__balance -= amount
        self.__history.append(("Withdraw", -amount))

    def get_balance(self):
        return self.__balance

    def show_transactions(self):
        balance = 0

        for action, amount in self.__history:
            balance += amount
            print(f"{action:<20} {amount:>10}    Balance = {balance}")

    def transfer_money(self, amount, destination):
        self.withdraw(amount)
        destination.deposit(amount)

    def update_balance(self, amount, description):
        self.__balance += amount
        self.__history.append((description, amount))


class Savings(Account):

    MIN_BALANCE = 500

    def __init__(self, holder_name, opening_balance, interest_rate):
        super().__init__(holder_name, opening_balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):

        remaining_balance = self.get_balance() - amount

        if remaining_balance < self.MIN_BALANCE:
            raise MinimumBalanceError(
                "Minimum balance of Rs.500 should be maintained."
            )

        self.update_balance(-amount, "Withdraw")

    def credit_interest(self):

        interest_amount = self.get_balance() * self.interest_rate

        self.update_balance(
            interest_amount,
            "Interest Added"
        )


class Current(Account):

    def __init__(self, holder_name, opening_balance, overdraft_limit):
        super().__init__(holder_name, opening_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        projected_balance = self.get_balance() - amount

        if projected_balance < -self.overdraft_limit:
            raise OverdraftExceededError(
                f"Maximum overdraft limit of Rs.{self.overdraft_limit} crossed."
            )

        self.update_balance(-amount, "Withdraw")


# Test 1 : Savings account 

print("Savings Account Test")

acc1 = Savings("Parth", 1000, 0.05)

acc1.deposit(500)

acc1.withdraw(900)

print("Current Balance =", acc1.get_balance())

try:
    acc1.withdraw(200)

except MinimumBalanceError as err:
    print(err)

# Test 2 : Current Account

print("\nCurrent Account Test")

acc2 = Current("Rahul", 500, 2000)

acc2.withdraw(2000)

print("Current Balance =", acc2.get_balance())

try:
    acc2.withdraw(600)

except OverdraftExceededError as err:
    print(err)



# Test 3 : Interest


print("\nInterest Calculation Test")

acc3 = Savings("Priya", 2000, 0.05)

acc3.credit_interest()

print("Balance after Interest =", acc3.get_balance())

acc3.show_transactions()



# Test 4 : Transfer


print("\nFund Transfer Test")

saving_acc = Savings("Amit", 1000, 0.05)

current_acc = Current("Neha", 500, 1500)

print("Before Transfer")
print("Savings =", saving_acc.get_balance())
print("Current =", current_acc.get_balance())

saving_acc.transfer_money(300, current_acc)

print("\nAfter Transfer")
print("Savings =", saving_acc.get_balance())
print("Current =", current_acc.get_balance())