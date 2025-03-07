"""
Anagram:
number = abc
n = len(abc)  
anagram = pow (a,n) + pow(b,n) + pow(c,n)
if number = anagram:
Number is an anagram!
"""

def anagram(number):
    n = len(str(number))
    temp = number
    sum = 0
    while temp != 0:
        # Get last digit
        LastDigit = temp % 10 
        # Finding lastdigit ^ count
        sum = sum + (LastDigit ** n)
        # Do floor division 
        # Get second last digit  
        temp = temp // 10
    if sum == number:
        print (f"{number} is an armstrong number")
    else: 
        print (f"{number} is not an armstrong number")


number = int(input("Enter a number: \n"))
result = anagram(number)

print(f"{result}")