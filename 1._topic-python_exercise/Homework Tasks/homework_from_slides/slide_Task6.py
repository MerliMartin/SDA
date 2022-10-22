"""
Write a function that takes two strings and checks to see if they are
anagrams of each other.
For example:
"Army" and "Mary",
"Sharing" and "Sunday",
"Quid est veritas?" and "Vir est qui adest",
"Jim Morrison" and "Mr. Mojo Risin"
"Tom Marvolo Riddle" and "I am Lord Voldemort"

NB! Anagram has to contain exactly the same amount of characters.
"""


def anagram_check(string_1, string_2):
    string_1 = sorted(string_1.lower().replace(" ", ""))
    string_2 = sorted(string_2.lower().replace(" ", ""))
    if string_1 == string_2:
        return "The 2 given words are anagrams!"
    else:
        return "The 2 given word are not anagrams!"


user_anagram_1 = input("Anagram Check! \nPlease Insert 1st anagram word: ")
user_anagram_2 = input("Please Insert 2nd anagram word: ")
print(anagram_check(user_anagram_1, user_anagram_2))
