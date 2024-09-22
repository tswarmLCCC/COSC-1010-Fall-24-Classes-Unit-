
## Abstraction Example: Simple Banking System

### 1. Customer Class


class Customer:
    def __init__(self, in_customer_id, in_name):
        self.customer_id = in_customer_id
        self.name = in_name

    def display_info(self):
        """
        Displays customer information.
        """
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")

# Example usage:
alice = Customer(in_customer_id=101, in_name="Alice Johnson")
alice.display_info()

bob = Customer(in_customer_id=102, in_name="Bob Jones")
bob.display_info()


### 2. Account Class


class Account:
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer  #this is the Customer Class, not a string
        self.balance = 0

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account.
        """
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")
    
    def getBalance(self):
        """
        Withdraws the specified amount from the account.
        """
        print(f"New balance: ${self.balance}")
        
# Example usage:
alice_account = Account(account_number=1001, customer=alice)
bob_account = Account(account_number=1002, customer=bob)
alice_account.deposit(1000)
alice_account.withdraw(300)
bob_account.deposit(1000)

alice_account.getBalance()
bob_account.getBalance()

### 3. Transaction Class (Optional)


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender  #sender here is another account!
        self.receiver = receiver  #another account
        self.amount = amount #and then the ammount

    def execute(self):
        """
        Simulates a transaction between two accounts.
        """
        if self.sender.balance >= self.amount:
            self.sender.balance -= self.amount
            self.receiver.balance += self.amount
            print(f"Transferred ${self.amount} from {self.sender.customer.name} to {self.receiver.customer.name}")
        else:
            print("Insufficient funds for the transaction.")

# Example usage:
bob = Customer(in_customer_id=102, in_name="Bob Smith")
bob_account = Account(account_number=1002, customer=bob)
transaction = Transaction(sender=alice_account, receiver=bob_account, amount=200)
transaction.execute()


bob_account.getBalance()
transaction = Transaction(sender=alice_account, receiver=bob_account, amount=200)
transaction.execute()
bob_account.getBalance()
