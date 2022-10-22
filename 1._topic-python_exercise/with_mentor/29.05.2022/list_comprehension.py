# in slide example
old_list = [1, 2, 3, 4, 5, 6, 7]
# even number, if not x % 2, it means if the value is 1, then it is False
new_list = [x ** 2 for x in old_list if not x % 2]
print(new_list)


# Mentor example
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = [x for x in list_num if x % 2 == 0]
print(even_number)


# ============================================================
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []


# square even value in main_list
def square_even(num_list):
    for i in num_list:
        if i % 2 == 0:
            even_list.append(i ** 2)
    return even_list


print(square_even(main_list))


# using list comprehension
# main_list1 = list(range(1, 31))
# even_list1 = [i**2 for i in main_list1 if i % 2 == 0]
even_longer_list = [x for x in range(1, 31) if x % 2 == 0]
# print(even_list1)
print(even_longer_list)