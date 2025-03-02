# Recursion = program where function calls itself again and again directly or indirectly. 
# Using Recursive algorithms, we can solve many problems. 

# Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.. 

def calculate_Fibonacci(i):
    if i == 0: 
        return 0
    elif i == 1:
        return 1
    else:
        return calculate_Fibonacci(i-2) + calculate_Fibonacci(i-1) 
        
index = int(input("Please enter the index till where you want me to write the series: "))
if index <= 0:
    print ("Please enter a positive number")
else:
    for i in range (0, index):
        print (calculate_Fibonacci(i))
