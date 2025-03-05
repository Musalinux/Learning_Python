# program for arithmetic operations:
# + + = +
# + - = -
# - - = +
# we will need to define a function
# we will need a list 
# we will need to tell the user to enter two signs, +, - seperated by commas - user_input.split (",")
# We will add this input to a dictionary. 
# then we will feed my_list [0] and my_list [1] to the def() 
# the def will then have logic to execute this. 
# 
# we will then return the value and tell = two postives added is positives. negatives is negative, positive negative is negative

def sum_of_signs():
    firstSign = add_to_list[0]
    secondSign = add_to_list[1]
    if firstSign == '+' and secondSign == '+':
        return '+'
    if firstSign == '+' and secondSign == '-' or firstSign == '-' and secondSign == '+':
        return '-'
    else:
        return '+'

while True: 
  user_input = input("Enter two signs '+' or '-' and I will tell sum of it: \n")
  if user_input.lower() == "stop":
    print ("End of program")
    break

  try: 
    add_to_list = user_input.split (",")
    convert_signs_to_str = str(user_input)
    print (add_to_list)
    result = sum_of_signs()

    print (f"The sum of {add_to_list[0]} and {add_to_list[1]} is {result}")
  except IndexError:
    print ("Invalid input! Please enter a two signs like '+' or '-'")