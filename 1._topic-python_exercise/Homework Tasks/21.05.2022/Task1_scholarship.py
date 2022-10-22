#  Estonia govt gives scholarship only to those with valid name and phone number
# implement a function to check if a username provided is correct
# ( must contain only alphabet -Hint use the isalpha() method) )
# and phone number is more than 10 characters
# if correct show message "congratulations you got the scholarship" otherwise show " You are not qualified"
def scholarship(name, phone_number):
    if name.isalpha() and len(phone_number) > 10:
        return "Congratulations you got the scholarship!"
    else:
        return "You are not qualified"


print("Hello!")
user_name = input("Name: ")
user_phone_number = input("Phone number: ")

print(scholarship(user_name, user_phone_number))
