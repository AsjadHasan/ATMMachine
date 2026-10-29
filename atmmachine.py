
"""Simulate an ATM machine with encapsulated balance management."""


class ATM:
    """Represent an ATM that allows validated withdrawals."""

    def __init__(self):
        """Initialize the ATM with a fixed balance of 5000 yen."""
        self.__balance = 5000

    def withdraw(self, amount):
        """Withdraw money if the amount is valid and funds are sufficient."""
        if amount <= 0:
            print("Please enter an amount greater than 0.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawal successful: ¥{amount}")
            print(f"Remaining balance: ¥{self.__balance}")

    def get_balance(self):
        """Return the current balance without allowing direct modification."""
        return self.__balance


def main():
    """Run the ATM terminal menu until the customer enters 0."""
    atm = ATM()

    print("Welcome to Fukuoka ATM!")
    print(f"Starting balance: ¥{atm.get_balance()}")

    while True:
        try:
            amount = int(input("\nEnter withdrawal amount (0 to exit): "))

            if amount == 0:
                print("Thank you for using Fukuoka ATM!")
                print(f"Final balance: ¥{atm.get_balance()}")
                break

            atm.withdraw(amount)

        except ValueError:
            print("Invalid input! Please enter a whole number.")


if __name__ == "__main__":
    main()
