#  implement a speed limit alert function for drivers in Estonia using their Distance and time.
# Note: Formula for Speed = Distance ÷ Time. the program takes as input the distance and time.
# if speed limit is between 0 - 20km/h show message "You are driving slow"
# if speed limit is between 21 - 45km/h show message "You are driving with the limit for inner streets"
# if speed limit is between 46 - 70km/h show message "You are driving faster. watch out for speed bumps"
# if speed limit is between 71 - 100km/h show message "You are driving very fast. Ensure you use your seat belt"
# if speed limit is above 100km/h show message "You are driving recklessly and putting your life at risk"

def speed_limit_alert(distance, time):
    speed = distance / time
    if 0 <= speed >= 20:
        message = "You are driving slow"
    elif 21 <= speed >= 45:
        message = "You are driving with the limit for inner streets"
    elif 46 <= speed >= 70:
        message = "You are driving faster. Watch out for speed bumps"
    elif 71 <= speed >= 100:
        message = "You are driving very fast. Ensure you use your seat belt"
    else:
        message = "You are driving recklessly and putting your life at risk"
    return message


user_distance = float(input("Please tell me your distance form the destination point: "))
user_time = float(input("Please tell me your arriving time to the destination point: "))
print(speed_limit_alert(user_distance, user_time))
