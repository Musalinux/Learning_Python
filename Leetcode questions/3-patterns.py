"""
Pattern 1: HashMap (Dictionary)
Problem: Find pairs, store previous values for quick lookups.
✔ Used in: Two Sum, Anagram Grouping, First Unique Character
"""
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

"""
Pattern 2: Sliding Window (Optimizing Loops)
Problem: Find the max sum in a subarray (instead of checking all possibilities).
✔ Used in: Maximum Subarray, Longest Substring Without Repeating Characters
"""
def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

"""
Pattern 3: Two Pointers
Problem: When dealing with sorted arrays or linked lists.
✔ Used in: Sorting problems, Linked Lists, Best Time to Buy/Sell Stock
"""
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
