"""
Count occurences of a character in a string.
Eg - "Logicops"
Char 'o' appears twice! 
"""

def occurence (mystring, mychar):
    count = 0
    for i in range (len(mystring)):
        if (mystring[i] == mychar):
            count += 1
    return count 

string = str (input ("Enter a string: \n"))
mystring = string.lower()

char = str (input ("Enter a character you want to check: \n"))
mychar = char.lower()

result = occurence(mystring, mychar)
print (f"The character '{char}' occurs {result} times in '{string}' ") 