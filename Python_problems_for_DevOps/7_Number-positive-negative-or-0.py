# Python program to fin if a number is positive negative or zero

def check_number(user_input):
  try:
        number = int(user_input)
        if number == 0:
            return "Zero"
        elif number > 0:
            return "Positive"
        else:
            return "Negative"
  except ValueError:
    return None
        
user_input = ""
while user_input.lower() != "stop":
    user_input = input("Enter the number and I will tell you if it is postive, negative, or 0\n ")
    
    if user_input.lower() == "stop":
        print ("End of program")
        break

    evaluation = check_number(user_input)

    if evaluation is not None:
        print (f"{user_input} is a {evaluation} number")
    else: 
        print("Invalid input! please enter a number or say stop and program will end")