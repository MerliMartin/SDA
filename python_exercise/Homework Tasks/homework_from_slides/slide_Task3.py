"""
Create a function that checks that the number given in the argument is
prime. The function should take a numeric value and return a logical
value of True / False.
E.g.
For 11 the function will return True, for 12 -> False.
"""


def prime_number(num):
    if num > 1:  # prime number can be positive number that is greater than 1
        for n in range(2, num):  # find numbers for dividing, num is not included
            if (num % n) == 0:  # if number num divides other numbers and the reminder is 0, it is not a prime number
                return False
            else:  # if there is only reminders that are greater than 0 then it is a prime number
                return True
        else:  # if it divides 1 and num itself, then it is a prime number, and they are not included to the range
            return True
    else:  # if num is 1 or smaller, then it is not a prime number
        return False


user_num = int(input("Check! Is your number prime or not ?: "))
print(prime_number(user_num))
