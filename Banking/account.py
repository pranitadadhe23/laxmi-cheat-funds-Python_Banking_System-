class BankAccount:
    account_counter =1000

    def __init__(self,name, balance=0):
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter+=1
        self.name = name
        self.__balance = balance #private variable only for account holder 
    
    def get_balance(self):
        return self.__balance
    
    def  withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawal of {amount} successful. Remaining balance is {self.__balance}")
            else:
                print("Insufficient balance")
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} successful. Remaining balance is {self.__balance}")
        else:
            print("Invalid amount")
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Account Holder:{self.name}, Account Balance :{self.__balance}")

class SavingAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.intrest_rate = interest_rate

    def calculate_interest(self):
        months = int(input("How many months to calculate interest"))
        interest = self.intrest_rate * months * self.get_balance()
        self.deposit(interest)
        print(f"Interest applied.{interest} New balance is {self.__balance}") 

class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=100000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit
        
