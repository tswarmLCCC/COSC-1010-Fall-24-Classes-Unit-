

## Abstraction Example: Simple Banking System

### 1. Customer Class

```python
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display_info(self):
        """
        Displays customer information.
        """
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")

# Example usage:
alice = Customer(customer_id=101, name="Alice Johnson")
alice.display_info()
```

### 2. Account Class

```python
class Account:
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer
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

# Example usage:
alice_account = Account(account_number=1001, customer=alice)
alice_account.deposit(1000)
alice_account.withdraw(300)
```

### 3. Transaction Class (Optional)

```python
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

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
bob = Customer(customer_id=102, name="Bob Smith")
bob_account = Account(account_number=1002, customer=bob)
transaction = Transaction(sender=alice_account, receiver=bob_account, amount=200)
transaction.execute()
```

### Conclusion

In this example, we've abstracted away the internal details of customer data, account balances, and transactions. Users can interact with the classes without worrying about the underlying complexity. Feel free to explore further by adding more features or customizing the behavior! 