def concatString(number):  
    result = ''
    for i in range (1,number+1):
        result = result + str(i)
    return result

user_input = input ("Enter a digit: \n")
number = int(user_input)
printString = concatString(number)
print (printString)