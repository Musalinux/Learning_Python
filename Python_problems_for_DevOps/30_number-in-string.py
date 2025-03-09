def numbers_in_string (text):
    number = []
    for word in text.split():
        if word.isdigit():
            number.append(word)
    return number
    
text = input("Enter a string with numbers: \n")
result = numbers_in_string(text)
print (f"The numbers in string are {result}")