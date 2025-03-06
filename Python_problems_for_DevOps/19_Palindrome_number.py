"""
Palindrome Number is = 121, 111, 141, 2442, etc. 
"""
def palindrome(nunber):
    palin = ""
    for i in str (number):
        palin = i + palin
    return int (palin)

number = int (input("Enter a number: \n")) 
reverse = palindrome(number)
if reverse == number:
    print (f"{number} is a palindrome number")
else:
    print (f"{number} is not a palindrome number")