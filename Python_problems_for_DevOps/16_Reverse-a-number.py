def reverse_string(user_input):
    result = ""
    for i in str(user_input):
      result = i + result 
    return int(result) 

user_input = int(input("Enter a set of numbers, I will reverse them: \n"))
reverse_string(user_input)
print(f"The reverse of {user_input} is {reverse_string(user_input)}")