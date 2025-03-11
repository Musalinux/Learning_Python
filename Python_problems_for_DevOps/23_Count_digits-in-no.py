"""
Here we will count the number of digits in a number. 
Wihout using the len() in built function. 
"""

def sumOfN(number):
    count = 0
    while (number > 0): 
        number = number // 10
        print (number)
        count = count + 1
    return count 
    
number = int(input("Enter a number: \n"))
result = sumOfN (number)

print (f"The number of digits in {number} is {result}")