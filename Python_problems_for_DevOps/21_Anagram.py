"""
Anagram? a word, name, or phrase formed by rearranging the letters of another. 
Eg: "Spar" is an anagram formed from "rasp"

sorted() = this functions returns an iterable list. 
for number = ascending order. 
for string = alphabetical order. s
for number + string = sorted() doesnt work. 
"""

def anagram(string1, string2):
    if sorted (string1) == sorted (string2):
        return True
    else:
        return False
    
string1 = input ("Please enter string 1: \n")
string2 = input ("Please enter string 2: \n")
string3 = sorted (string1)

print (string3)

if anagram(string1, string2):
    print ("This is an anagram")
else:
    print ("This is not an anagram")

