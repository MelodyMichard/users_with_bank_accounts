class BankAccount:
        def __init__(self, int_rate, balance):
                self.int_rate = int_rate
                self.balance = balance

        def deposit(self, amount):
                self.balance += amount
                return self

        def withdraw(self, amount):
                if(self.balance - amount) >= 0:
                        self.balance -= amount
                else:
                        print(f"Insufficient Funds: A $5 fee has been charged")
                self.balance -= 5
                return self

        def display_account_info(self):
                return f"Balance: {self.balance}"

        def yield_interest(self):
                if self.balance > 0:
                    self.balance += (self.balance * self.int_rate)
                return self

class User:
        def __init__(self, name):
                self.name = name
                self.account = BankAccount(int_rate=.02, balance=0)

        def display_user_balance(self):
                print(f"User: {self.name}, Balance: {self.account.display_account_info()}")
                return self

tom = User("Tom")

tom.account.deposit(100)
tom.display_user_balance()
