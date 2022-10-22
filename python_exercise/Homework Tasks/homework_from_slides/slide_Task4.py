"""
Create a function that checks if the string given as an argument is a
palindrome (ie reading backwards and forwards is exactly the same, eg
"kayak", "madam")
"""


def palindrome_check(word):
    word = word.upper().strip()  # I made it uppercase because, it is better to distinguish a word
    reverse_word = word[::-1]
    if word == reverse_word:
        return f"{word} is a palindrome!"
    else:
        return f"{word} is not a palindrome! Reading {word} backwards is {reverse_word}!"


user_word = input("Hello! \nPlease give me a palindrome word: ")
print(palindrome_check(user_word))
