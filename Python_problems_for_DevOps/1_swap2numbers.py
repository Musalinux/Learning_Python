# Swapping 2 numbers without a vairable.

def swap_number(num1, num2):
    if num1 < num2:
        print("Here is the list of items you have given", num1, num2)
        num2 = num2 + num1 # 30
        num1 = num2 - num1 # 20 
        num2 = num2 - num1 # 
        print("Here is the swapped list", num1, num2)
    elif num1 > num2:
        print("Here is the list of items you have given", num1, num2)
        num1 = num1 + num2
        num2 = num1 - num2 
        num1 = num1 - num2 
        print("Here is the swapped list", num1, num2)

user_input = input("Enter 2 numbers you want to swap, I will do it for you!")
add_input_to_list = user_input.split(",")
print(add_input_to_list)
num1 = int(add_input_to_list[0])
num2 = int(add_input_to_list[1])
swap_number(num1, num2)