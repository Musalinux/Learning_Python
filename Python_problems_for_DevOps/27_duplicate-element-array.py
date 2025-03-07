"""
Array = a collection (list) of similar type of items (eg: int)
"""

my_array = [10,20,30,40,40,50,10,70,30,20,50,100,20,100]
temp_set = set(my_array)
dup_array = list(num for num in temp_set if my_array.count(num) >1)
print (f"The duplicate numbers in the array are: {dup_array}")