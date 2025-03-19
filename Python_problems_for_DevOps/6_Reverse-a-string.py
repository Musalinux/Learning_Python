# Reverse a string 
def str_rev (Mystring):
    reverseString = ""
    for i in MyString:
        reverseString = i + reverseString
    return reverseString

MyString = input("Enter a string and I will reverse it for you: \n")

reversed_string = str_rev(MyString)
print (f"Reverse of {MyString} is '{reversed_string}' ")