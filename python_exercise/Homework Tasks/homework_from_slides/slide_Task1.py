"""
Write a program that will convert the sequence of numbers entered by
the user into text, e.g .:
112 -> "one one two"
9973 -> "nine nine seven three"
Hint: you need the input () function, a dictionary and a loop.
"""
num_words = {
    "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
    "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
}


def print_num_words(number):
    var_words = ""
    for x in number:
        var_words += (num_words.get(x) + " ")
    return var_words


user_number = input("Give me numbers: ")
print(print_num_words(user_number))
