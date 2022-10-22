# design simple calender
# monday - 1 to sunday - 7
# def weekday_check(weekday_num):
#     if weekday_num == 1:
#         return f"The {weekday_num}'st day is Monday"
#     elif weekday_num == 2:
#         return f"The {weekday_num}'nd day is Tuesday"
#     elif weekday_num == 3:
#         return f"The {weekday_num}'rd day is Wednesday"
#     elif weekday_num == 4:
#         return "The 4'th day is Thursday"
#     elif weekday_num == 5:
#         return "The 5th day is Friday"
#     elif weekday_num == 6:
#         return "The 6th day is Saturday"
#     elif weekday_num == 7:
#         return "The 7th day is Sunday"
#     else:
#         inv_numb = int(input(f"{weekday_num} is invalid, please enter number 1 to 7: "))
#         return weekday_check(inv_numb)
#
#
# user_weekday = int(input("Please insert weekday number: "))
# print(weekday_check(user_weekday))


# ===============================================================================================
# using dictionaries
days = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday"}
user_day = input("Please enter the number of weekday: ")
if user_day in days:
    print(days.get(user_day))
else:
    inv_number = input(f"{user_day} is invalid weekday! Please enter correct (we have 7 days in the week): ")
    print(days.get(inv_number))
