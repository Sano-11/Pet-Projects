class SecureBankAccount:
    def __init__(self, account_number: str, initial_balance: float, pin: str):
        # Initializing private properties with an underscore
        self._account_number = account_number
        self._balance = initial_balance
        self._pin = pin
        self._is_locked = False

    def get_account_number(self) -> str:
        return self._account_number

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if not self._is_locked:
            self._balance += amount

    def withdraw(self, amount: float, entered_pin: str) -> str:
        if self._is_locked:
            return "Account is locked. Withdrawal not allowed."
        
        if entered_pin != self._pin:
            return "Incorrect PIN."
        
        if amount > self._balance:
            return "Insufficient balance for withdrawal."
        
        self._balance -= amount
        # Added :.2f here to ensure two decimal places in the success message
        return f"Withdrawal successful. New balance: {self._balance:.2f}"

    def lock_account(self) -> None:
        self._is_locked = True

    def __str__(self) -> str:
        # P prefix added and :.2f used for 2 decimal places
        return f"{self._account_number} - P{self._balance:.2f} - {self._is_locked}"