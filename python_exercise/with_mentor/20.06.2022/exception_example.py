class CustomException(Exception):
    def __init__(self):
        self.value = "Zero is not allowed"

    def __str__(self):
        return repr(self.value)


a = 91
b = [0, 8, 2]

for i in b:
    if i == 0:
        raise CustomException()
    result = a / i
    print(result)

# a = 91
# b = [0, 8, 2]
#
# for i in b:
#     try:
#         result = a / i
#     except ZeroDivisionError:
#         print("Division by zero is not allowed")
#         continue
#     print(result)


# x = [2, 5, 7, 10]
# user_num = int(input("Give me number! "))
#
# try:
#     user_num < len(x)
# except IndexError:
#     print("We don't have that many numbers in list.")
# print(f"the list length is {len(x)} and the number is {x[user_num]}")
