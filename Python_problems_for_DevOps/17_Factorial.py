def factorial(num):
    factorial = 1
    while num != 0:
        factorial = factorial * num
        num -= 1
        # or num = num -1
    return factorial

num = int(input("Enter a number \n"))
factorial(num)

print(f"Factorial of {num} is {factorial(num)}")