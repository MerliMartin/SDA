"""
Function to check account transfer
"""

import time

user_balance = int(input("Provide your current account balance? "))
user_transfer_amount = int(input("Provide your transfer amount? "))
loan_amount = 250


def confirm_balance(func):
    # a decorator that only calls a decorated function at certain times
    def wrapper():
        if (user_balance - loan_amount) > user_transfer_amount:
            print("Checking the transaction details.... ")
            time.sleep(1.0)  # use to simulate checking delay process
            print("...Sending validated.. Now transferring amount  :)")
            time.sleep(1.0)
            print(f"Your new account balance is {(user_balance - loan_amount) - user_transfer_amount}")
            return func()
        else:
            print("Account balance is insufficient to complete transaction")

    return wrapper


@confirm_balance
def transfer_transaction():
    print("...Thank you for banking with us at LHV...Have a nice day :)")


transfer_transaction()
# confirm_balance(transfer_transaction)
