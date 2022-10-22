# Compare greatest of 3 numbers ()
def max_of_three_numbers(a, b, c):
    # If a value is bigger than b and c, then it shows a value, if not, then python checks other conditions
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


# Asks the user for numbers, it has to be integer, other values shows errors.
user_a = int(input("Enter first number: "))
user_b = int(input("Enter second number:    "))
user_c = int(input("Enter third number: "))

xx = max_of_three_numbers(user_a, user_b, user_c)
print(f'The greatest number is {xx}')  # f-string to print the variable
