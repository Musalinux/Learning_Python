"""
Problem: Given a binary tree, check if the tree follows an "Even-Odd" structure:
✔ Even-indexed levels (0, 2, 4…) must have strictly increasing odd values.
✔ Odd-indexed levels (1, 3, 5…) must have strictly decreasing even values.

Concepts Used: BFS, Level Order Traversal
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_even_odd_tree(root):
    queue = deque([(root, 0)])  # (Node, Level)
    
    while queue:
        level_values = []
        for _ in range(len(queue)):
            node, level = queue.popleft()
            
            # Check for even-odd conditions
            if level % 2 == 0 and (node.val % 2 == 0 or (level_values and node.val <= level_values[-1])):
                return False
            if level % 2 == 1 and (node.val % 2 == 1 or (level_values and node.val >= level_values[-1])):
                return False
            
            level_values.append(node.val)
            
            # Add children
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
    
    return True

# Example Usage
root = TreeNode(1, TreeNode(10, TreeNode(3), TreeNode(7)), TreeNode(4, TreeNode(9), TreeNode(2)))
print(is_even_odd_tree(root))