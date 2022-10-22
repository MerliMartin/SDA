"""
Write a program that returns the absolute value of a number retrieved
from the user. The program should keep asking for this number until it is
correctly given.
Remember that the user may not always enter a numeric value, but may
also enter, for example, "cauliflower". Check what happens then and be
sure to handle exceptions.
"""

if __name__ == "__main__":
    while True:
        try:
            number = float(input("Enter a number \n"))
            print(f"The absolute value of {number} is {abs(number)}")
            break
        except ValueError:
            print("Cannot return absolute value for the specific input!")
