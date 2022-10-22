from datetime import datetime


def disable_at_night(func):
    def wrapper():
        if datetime.now().hour < 18:
            func()

    return wrapper


@disable_at_night
def say_something():
    print("Hello, welcome to our hotel")


say_something()
