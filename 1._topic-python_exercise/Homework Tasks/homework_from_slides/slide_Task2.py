"""
Create a function that takes a list of integers and returns what the
smallest number is in.
Do not use built-in functions.
eg. for the list [42, 13, 56, 7, 12, 3, 85] the function should return 3, because
the smallest element is found at this index in this list.
"""


def min_num_in_list(list_numbers):
    smallest = list_numbers[0]
    for num in range(len(list_numbers)):
        if list_numbers[num] < smallest:
            smallest = list_numbers[num]
    return smallest


list_ints = [42, 13, 56, 7, 12, 3, 85]
print(min_num_in_list(list_ints))
# new_list = [17, 2, 1, 16, 2]
# print(min_num_in_list(new_list))
