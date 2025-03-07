"""
Insert a number at an index in an array. 
array = [1,2,3,4] 
insert at index [1] = 5
array = [1,5,2,3,4]
"""

def insertindex(number, index):
    my_array = [1,2,3,4,5]
    if index >= len (my_array):
        print ("The number is out of range")
    else: 
        my_array.insert(index, number)
    return my_array

my_array = [1,2,3,4,5]
print (my_array)
number = int(input("Enter a number to insert in the array: \n"))
index = int (input("Enter the index where you want to add this number: \n"))

new_array = insertindex(number, index)
print (f"The new array is {new_array}")