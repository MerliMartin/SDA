"""
1. funktion takes a number e.g 8
2. prints the number 8
3. subtracts 1 from the number 8 - number is now 7
4. checks if the number 7 is 5, it's not, then false,
5. if false then goes to beginning of the loop and prints the number 7
6. subtracts 1 from the number 7 - number is now 6
7. checks if the number 6 is 5, it is not, it means false
8. when false again then goes to the beginning of the loop and prints the number 6
9. subtracts 1 from the number 6 - it is now 5
10. checks if the number 5 is 5, it is, then true
11. when true, then breaks the while loop - doesn't go back to the beginning of the loop
12. from outside the while loop there is print "Lift off!"
13. There is nothing more for the code to do!
"""


def premature_lift_off(number):
    while number:
        print(number)
        number -= 1
        if number == 5:
            break
    print("Lift off!")


premature_lift_off(8)
