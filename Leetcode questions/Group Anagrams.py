"""
Problem: Given a list of words, group words that are anagrams of each other.
"""
from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    
    for word in words:
        sorted_word = "".join(sorted(word))  # Sort letters to identify anagrams
        anagrams[sorted_word].append(word)  # Group words with the same sorted form
    
    return list(anagrams.values())  # Return grouped anagrams

# Example Usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
