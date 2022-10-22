import weekday

user_day = input("What holiday day of the week you worked?: ")
user_hourly_wage = int(input("What is your hourly wage?: "))
# It works when user works 160h in month
total_pay = (user_hourly_wage * 160) + weekday.StaffBenefit(user_day, user_hourly_wage).weekdays_with_benefit()
print(total_pay)
