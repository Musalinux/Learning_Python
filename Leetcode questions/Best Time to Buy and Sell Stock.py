"""
Problem: Given a list of stock prices, find the maximum profit you can make by buying & selling once.
Concepts Used: Greedy Algorithm, Single Pass
"""
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)  # Track the lowest price seen so far
        max_profit = max(max_profit, price - min_price)  # Maximize profit
    
    return max_profit

# Example Usage
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices)) 