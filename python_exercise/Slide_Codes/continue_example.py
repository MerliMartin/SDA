"""
1. function takes a number e.g 4
2. while number is 4
3. then subtracts 1 from the number 4 - it is now 3
4. checks if the number 3 reminder is 0 or 1 - 3%2 is 1 - it means it is true
5. if true then it continues - meaning it leaves out the number 3
6. goes back to beginning of the while loop
7. then subtracts 1 from the number 3 - it is now 2
8. checks if the number 2 reminder is 0 or 1 - 2%2 is 0 - it means it is false
9. if false, then it is going to print the number 2 (print is located in the else: block)
10. no it can go back to the beginning of the while loop
11. subtracts 1 from number 2 - the number is now 1
12. checks if the number 1 reminder is 0 or 1 - 1%2 is 1 - it means it is true
13. if true then it means it leaves out the number 1 - and goes back to the beginning of the loop
14. then subtracts 1 from the number 1 - it is now 0
15. then it checks the reminder of the 0 - it is 0 - it means it is false
16. the number 0 goes to the else: block and print out the number 0
17. while loop iterates to 0, not below 0 or example if we want to add number,
and when we don't have condition for ending the while loop , it iterates as long as the computer runs out of the memory?
18. N.B. 0 means False and 1 means True
19. "if number % 2" is the same as  "if number % 2 == 1" if function is True by default
20. e.g. if we want that the reminder is 0, the 0 is false,
we have to tell if-condition that: "if number % 2 == 0" or " if not number % 2"
"""


def even_count_down(number):
    while number:
        number -= 1
        if number % 2:
            continue
        print(number)


print("The first code output! - even number count-down")
even_count_down(4)


def odd_count_down(num):
    while num:
        num -= 1
        if not num % 2:
            continue
        print(num)


print("The second code output! - odd number count-down")
odd_count_down(4)
