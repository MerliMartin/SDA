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
    upper_case_letters = ""
    lower_case_letters = ""
    for letter in words:
        if letter == letter.upper():
            upper_case_letters += letter
            upper_case_letters = upper_case_letters.strip()
        else:
            lower_case_letters += letter
    count_upper_case_letters = len(upper_case_letters)
    count_lower_case_letters = len(lower_case_letters)
    return f"You have {count_upper_case_letters} upper case letter(s) and " \
           f"{count_lower_case_letters} lower case letter(s)!"


user_words = input("Give me words, and let them be upper and lower cases!: ")
print(count_letters(user_words))
