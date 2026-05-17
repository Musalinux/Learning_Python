import sys 

def add (num1, num2):
    output = num1 + num2
    return output 


num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    result = add (num1, num2)
    print (result)