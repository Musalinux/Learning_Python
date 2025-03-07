"""
Perfect Number: is a positive integer which is a sum of its positive divisors, 
excluding the number itself.

Eg: 6 -> 3,2,1 -> 3 + 2 + 1 = 6 
"""

def perfect_number(num):
    sum = 0
    for i in range (1, (num // 2) +1):
        rem = num % i
        if rem == 0:
            sum = sum + i 
    if sum == num:
        print (f"{num} is a perfect number")
    else:
        print (f"{num} is not a perfect number")

num = int(input("Enter a number: \n"))
perfect_number(num)