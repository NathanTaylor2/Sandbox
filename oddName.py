"""
Name: Nathan Taylor
"""
user_name = input("Please input your name.")
second_letter = ""
if user_name == "":
    user_name = input("Please input your name")
print(user_name[::2])