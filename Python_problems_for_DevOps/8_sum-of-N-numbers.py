# sum of N numbers = n(n+1)/2

def sum_of_numbers(n):
  if n == 0:
    print ("Enter a number more than zero")
    return None 
  if n  % 1 != 0:
    return "Please enter a whole number"
  
  return int(n * (n + 1) // 2)

user_input = ""

while True: 
    user_input = input("Enter any number to get sum (or type 'stop' to exit): ")
    
    if user_input.lower() == "stop":
      print ("Program exited")
      break 

# Here rather than returning value directly, we will try execution.
# this prevents the program from breaking. 
    try: 
      n = float(user_input)
      if n <= 0:  # Stop execution if the number is not positive
          print("Enter a positive number")
          continue  
        
      result = sum_of_numbers(n)
      
      if result is not None: # We will print output only for valid numbers. 
        print (f"The sum of {user_input} numbers is {sum_of_numbers(n)}")
    except ValueError:
      print ("Invalid input! Please enter a number")