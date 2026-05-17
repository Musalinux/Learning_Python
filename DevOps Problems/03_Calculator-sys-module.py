import sys 

def add (num1, num2):
    output = num1 + num2
    return output 

def sub (num1, num2):
    output = num1 - num2
    return output 

def mul (num1, num2):
    output = num1 * num2
    return output 

def div (num1, num2):
    output = num1 // num2
    return output 

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    result = add (num1, num2)
    print (result)
elif operation == "sub":
    result = sub (num1, num2)
    print (result)
elif operation == "mul":
    result = mul (num1, num2)
    print (result)
elif operation == "div":
    result = div (num1, num2)
    print (result)