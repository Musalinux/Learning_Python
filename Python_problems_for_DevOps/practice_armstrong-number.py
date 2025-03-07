"""
Armstrong number: 
153 = 1x1x1 + 5x5x5 + 3x3x3  
"""
def armstrong(number):
    n = len(number)
    sum = 0
    temp = number
    while temp != 0:
        LastDigit = temp % 10 
        sum = sum + (LastDigit ** n)
        temp = temp // 10 
    return sum 

number = int(input("Please enter a number: \n"))
result = armstrong(number)
if number == sum:
    print (f"{number} is an armstrong number")
else:
    print (f"{number} is not an armstrong number")