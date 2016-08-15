"""
Name: Nathan Taylor
"""


def main():
    user_name = get_name()
    print(user_name[::2])


def get_name():
    user_name = input("Please input your name.")
    if len(user_name) < 1:
        user_name = input("Please input your name")
    return user_name


main()
