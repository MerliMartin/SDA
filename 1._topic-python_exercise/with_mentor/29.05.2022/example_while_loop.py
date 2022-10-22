"""
while <expression>:
    <statement(s)>
1...5
counter >> know when to stop
"""
n = 0
while n < 5:
    n += 1
    print(n, end=' ')  # prints to one line and there is space between the numbers


# =========================================
# Slide example while loop
def count_down(number):
    while number:
        print(number)
        number -= 1
    print("Lift off!")


count_down(11)


# ============================================


