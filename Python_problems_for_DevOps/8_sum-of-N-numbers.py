# sum of N numbers = n(n-1)/2

def sum_of_numbers(n):
  if n == 0:
    print ("Enter a number more than zero")
  if n  % 1 != 0:
    return "Please enter a whole number"

  result = int(n * (n + 1) // 2)
  return result


user_input = input("Enter any number and I will give you the sum of all numbers till that number: ")


try: 
  n = float(user_input)
  evaluate = sum_of_numbers(n)
  print (f"The sum of {user_input} numbers is {sum_of_numbers(n)}")
except ValueError:
  print ("Invalid input! Please enter a number")