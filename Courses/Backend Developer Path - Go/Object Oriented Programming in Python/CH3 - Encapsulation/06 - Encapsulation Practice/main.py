class BankAccount:
    def __init__(bank, account_number: str, initial_balance: float):
        bank.__account_number = account_number
        bank.__balance = initial_balance


    def get_account_number(bank) -> str: return bank.__account_number
    def get_balance(bank) -> float: return bank.__balance


    def deposit(bank, amount: float):
        if amount <= 0: raise ValueError("cannot deposit zero or negative funds")
        bank.__balance += amount


    def withdraw(bank, amount: float):
        if amount <= 0: raise ValueError("cannot withdraw zero or negative funds")
        if amount > bank.get_balance(): raise ValueError("insufficient funds")
        bank.__balance -= amount
