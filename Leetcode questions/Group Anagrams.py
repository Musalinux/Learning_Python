from collections import defaultdict

def group_anagrams (strs): 
    anagrams = defaultdict (list)
    for word in strs: 
        key = "".join(sorted(word))
        anagrams[key].append(word)
    return list (anagrams.values())

user_input = input ("Enter list of stringsL: \n")
strs = (word.strip() for word in user_input.split(","))

result = group_anagrams (strs)

print ("Grouped anagrams are:")
for group in result:
    print (group)