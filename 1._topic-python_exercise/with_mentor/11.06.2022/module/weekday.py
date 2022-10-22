class StaffBenefit:
    def __init__(self, day, hourly_wage):
        self.hourly_wage = hourly_wage
        self.day = day
        self.days = {
            "1": "Monday",
            "2": "Tuesday",
            "3": "Wednesday",
            "4": "Thursday",
            "5": "Friday",
            "6": "Saturday",
            "7": "Sunday"
        }

    def weekdays_with_benefit(self):
        if self.day in self.days:
            if self.day == "5":
                benefit = 1.5 * self.hourly_wage
                return benefit
            elif self.day == "6" or self.day == "7":
                benefit = 2.5 * self.hourly_wage
                return benefit
            else:
                benefit = 0.5 * self.hourly_wage
                return benefit


if __name__ == "__main__":
    user_day = input("What day of the week?: ")
    user_hourly_wage = int(input("What is your hourly wage?: "))
    user_object = StaffBenefit(user_day, user_hourly_wage)
    weekday_benefit = user_object.weekdays_with_benefit()
    weekday = user_object.days.get(user_day)
    print(f"You will get benefit {weekday_benefit}€, when you work on {weekday}")
