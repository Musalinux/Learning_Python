def is_leap (year):
    if year % 4 == 0 and year % 400 == 0:
        return (f"{year} is a leap year")
    if year % 4 == 0 and year % 100 == 0:
        return (f"{year} is not a leap year")
    elif year % 4 == 0: 
        return (f"{year} is a leap year")
    return (f"{year} is not a leap year")

while True:
    user_input = input("Enter a year, I will tell you if it is a leap year or not: \n")
    if user_input.lower() == "stop":
        print ("End of program")
        break
    try:
      year = int (user_input)
      check_leap = is_leap(year)
      print(is_leap(year))
    except ValueError:
     print("Invalid input! Please enter a year")