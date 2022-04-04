# Create a bank account class
# think about what methods you might need (and ones you definitely don't need)
# what can go wrong
# what exceptions you might want to raise, based on invalid input
# transfer to self amount recipient

class BankAccount:
    def __init__(self, a=0, i=0.1):
        self.__interest_rate = i
        self.__account_balance = a + (a * i)

    def get_account_balance(self):
        return self.__account_balance

    def credit_account(self, a=0):
        self.__account_balance = self.__account_balance + a

    def debit_account(self, a=0):
        if a >= 0:
            bal = self.__account_balance - a
            if bal < 0:
                raise ValueError("Insufficient balance")
            else:
                self.__account_balance = bal
                return True
        else:
            raise ValueError("Positive amount required")

    def get_interest(self):
        return self.__interest_rate

    def transfer(self, amount, recipient):
        if self.debit_account(amount):
            recipient.credit_account(amount)


# Test
account_one = BankAccount(100)
account_two = BankAccount(100)

try:
    account_one.transfer(-500, account_two)
except ValueError as v:
    print(v)

print(account_one.get_account_balance())
print(account_two.get_account_balance())

# print(account_one.get_account_balance())
# try:
#     account_one.debit_account(-1000)
# except ValueError as v:
#     print(v)
# print(account_one.get_account_balance())
