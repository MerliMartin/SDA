"""
1) create a list using range of number from 1 to 30
    i) divide the list into two equal sub-list x1 and x2
    ii) reverse the sub list x2
    iii) print out the length of sub-list x2
2) write a program to take a string from the user
    i) determine the middle position of the string provided by the user and print it out
    ii) add to the input provided by the user the word "Thank you" and print it out
"""

# 1)
x = list(range(1, 31))
# 1) - i)
x1 = x[:15]
x2 = x[15:]
# 1) - ii)
x2 = x2[::-1]
# 1) - iii)
x2_length = len(x2)
print(x2_length)
# =======================
x = list(range(1, 31))
# x1 = x[:15]
# x2 = x[15:]
print(f'x1: {x1}')
# print("x: ", x1)
print(f'x2: {x2}')
# reverse list x2
x2.reverse()
print(x2)
# length of sub-list x1
print(len(x1))
# =======================
# 2)
user_string = str(input("Please insert your letters: "))
# 2) - i)
# --- Mentor solution
print(len(user_string))
middle = len(user_string) // 2
print(f"The middle letter is {user_string[middle]} at position {middle}")
print(user_string + " Thank you")
# --- End of Mentor solution
