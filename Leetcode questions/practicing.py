def two_sum (nums, target): 
    hashmap = {}
    for i, num in enumerate (nums): 
        diff = target - num 
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return ("No numbers add to the target")
        
user_input = input ("Enter a list of numbers seperated by commas: \n")
nums = [int(x.strip()) for x in user_input.split(",")]

target = int (input("Enter a target: \n"))

result = two_sum (nums, target)

if isinstance (result, list):
    index1, index2 = result
    num1, num2 = nums[index1], nums[index2]
    print (f"{num1} + {num2} = {target}")
    print (f"indexes are: {index1} and {index1}")
else:
    print (result)