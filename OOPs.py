class BankAccount:
    
    bank_name = "ABC Bank"   # class variable
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
    
    def __str__(self):
        return f"{self.name} → Balance: {self.balance}"


def main():
    name = input("Enter name: ")
    balance = int(input("Enter initial balance: "))

    acc = BankAccount(name, balance)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            amount = int(input("Enter amount: "))
            acc.deposit(amount)
        elif choice == "2":
            amount = int(input("Enter amount: "))
            acc.withdraw(amount)
        elif choice == "3":
            print(acc)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


main()