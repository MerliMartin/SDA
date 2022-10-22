# task
# a function to say if person is male or female
# ask the user for age
# height
# if age > 25 and height is > 50 then this is male
# otherwise this is female
# print out that output to the user
def gender(age, height):
    if age > 25 and height > 50:
        return "male"
    else:
        return "female"


user_age = float(input("How old are you? "))
user_height = float(input("What is your height [cm]? "))
user_gender = gender(user_age, user_height)
print(f"You are {user_gender}!")
