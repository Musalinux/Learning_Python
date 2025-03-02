# Iterative - Here we will iterate through each number and calculate. 
# Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.. 

index = int("Enter the index till which you want me to write a Fibonacci Series")

FirstNumber = 0
SecondNumber = 1
temp = 0

print (FirstNumber)
print (SecondNumber)
for i in range (0, index):
    temp = FirstNumber + SecondNumber
    FirstNumber = SecondNumber
    SecondNumber = temp
    print (temp)