# my_dict = {'a': "one", 'b': "two", 'c': "three"}
#
#
# # print(my_dict)
# my_dict['d'] = "four"  # adding new key and value to the dictionary
# print(my_dict)
#
# print(my_dict['a'])  # use the key to get the value
# print(my_dict.get('a'))  # use the key to get the value
#
# print(f"using [] {my_dict['b']}")
#
#
# # use .get - because it doesn't give unnecessary errors, if i don't have the key and value in dic
# print(f"using get {my_dict.get('e')}")
#
# # --- other example
# country_capital = {"Estonia": "Tallinn", "Lithuania": "Vilnius", "Latvia": "Riga", "Belarus": "Minsk"}
# print(country_capital)
# print(country_capital["Estonia"])
#
# # adding a new key-value pair - Russia
# country_capital["Russia"] = "Moscow"
# print(country_capital)

# Task
"""
Create a phone book with important services in Estonia - dic
1) Fireservice: 112, police: 911, kfc, ambulance, boltfood, seb, Tele2,
2) ask the user for the service they need ... then print dialing(key)
"""
# 1)
service_phonebook = {
    "fireservice": 112,
    "police": 911,
    "kfc": 972,
    "ambulance": 112,
    "boltfood": 1414,
    "seb": 227,
    "tele2": 9876}
# 2)
user_service = input("What service you need? ")
lower_case_user_service = user_service.lower()  # because I have stored service names in lower case's
control_word = lower_case_user_service in service_phonebook  # checks if the word is in the phone book

if control_word:  # by default, it is True
    print(f"The phone number is {service_phonebook.get(lower_case_user_service)} for {user_service}.")
else:  # if user asked number that isn't in the phone book
    print(f"We don't have {user_service} number")

list(service_phonebook.keys())  # the keys
list(service_phonebook.values())  # the values
list(service_phonebook.items())  # combination of key and value
