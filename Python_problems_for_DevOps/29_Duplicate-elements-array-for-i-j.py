def duplicates_in_array():
    my_array = [10,20,30,40,40,50,10,70,30,20,50,100,20,100]
    print ("The duplicates in array are: \n")
    arr_len = len(my_array)
    
    # search for all duplicate elements: 
    for i in range (0, arr_len):
        for j in range (i+1, arr_len):
            if (my_array[i] == my_array[j]):
                print (my_array[j])

# Driver code 
duplicates_in_array()