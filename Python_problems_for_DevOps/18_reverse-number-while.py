def reverse_string(num):
    result = 0
    while num != 0:
        last_digit = num % 10
        result = result * 10 + last_digit
        num = num // 10 # Floor division : 15/2 = 7.5 -> 7
    return result 
 
num = int(input("Enter a set of numbers, I will reverse them: \n"))
reverse_string(num)
print(f"The reverse of {num} is {reverse_string(num)}")