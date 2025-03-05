def primeOrNot (number):
    if number == 1:
      return "not a prime number"
    for i in range (2, number):
        if (number % i == 0):
            print ("not a prime number") 
            break
    else: 
        return "a prime number"
        
user_input = ""
while True:
  user_input = input ("Enter a number, I will tell you if it is a prime number: \n")
  if user_input.lower() == "stop":
    print ("End of program")
    break 
  try:
    number  = int(user_input)

    if number >  0:
        result = primeOrNot(number)
        print (f"{number} is {result}")
  except ValueError:
    print ("Invalid input! Please enter a number")