"""
Create a function that will calculate the number of upper and lower case
letters in a string.
e.g. for: "The quick Brown Fox"
expected result:
Number of uppercase letters: 3, number of lowercase letters : 13
Hint: use a loop, conditional statement, and appropriate methods for the
string
"""


def count_letters(words):
    count_lower_case = 0
    count_upper_case = 0
    for letter in words:
        if letter == letter.lower():
            count_lower_case += 1
        else:
            count_upper_case += 1
    return f"You have {count_lower_case} lower case letters and {count_upper_case} upper case letters"


user_word = input("Hei! \nGive me different words with upper and lower cases!: ")
user_word = user_word.strip()
print(count_letters(user_word))
