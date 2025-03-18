# We need to find the length of a string without using the "len" in-built function. 
# To do this, we will be making our own method of finding the length of a given string.


def str_length(myString):
    len_count = 0
    for i in myString:
        len_count = len_count + 1
    return len_count

myString = input("Enter the string you want to find the length of\n ")

result = str_length(myString)
print ("This is the length of the given string: ", result)