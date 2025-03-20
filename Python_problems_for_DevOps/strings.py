"""
Question 2: String Slicing
Write a Python program that takes a string as input and prints the following:

The first 5 characters of the string.

The last 5 characters of the string.

The middle 3 characters of the string (if the string has an odd length).
"""


def printer(user_input):
    length = len (user_input)
    if length > 5 and length % 2 ! = 0:
        print(user_input)
        print(f"The first 5 characters are: {user_input[0:5]}")
        print(f"The last 5 characters are: {user_input[-5:]}")
        char = len(user_input)
        char = char // 2
        mid3char = user_input[char - 1:char + 2]
        print(f"The middle 3 characters are: {mid3char}")
    else:
        print("please enter a string with length odd and more than 5")


user_input = input("Enter a string: \n")
printer(user_input)