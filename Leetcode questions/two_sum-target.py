def two_sum (nums, target): 
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return ("No numbers add to the target")

give_numbers = input ("Enter numbers separated by commas: \n")
nums = [int(x.strip()) for x in give_numbers.split(",")]

target = int (input ("Enter a target: \n"))

result = two_sum (nums, target)

if isinstance (result, list):
    index1, index2 = result
    num1, num2 = nums[index1], nums[index2]
    print (f"{num1} + {num2} = {target}")
    print (f"Indexes: {index1} and {index2}")
else: 
    print (result)