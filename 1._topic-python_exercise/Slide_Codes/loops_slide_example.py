# for loop example 1 - find the largest number in
def my_max(sequence):
    largest = 0
    for element in sequence:
        if element > largest:
            largest = element
    return largest


max_number = (1, 5, 0, 4, 9, 17, 10)
print(my_max(max_number))
print(max((1, 5, 0, 4, 9, 17, 10)))  # max function does the same as my def my_max
# =======================
