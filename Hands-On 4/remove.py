def remove_duplicates_elements(array):
    if len(array) == 0:
        return array
    
    unique_index = 0    #Tracks the last position of unique elements in the array.
    
    for current_index in range(1, len(array)):   #Iterates through the array to find new unique elements.
        if array[current_index] != array[unique_index]:
            unique_index += 1
            array[unique_index] = array[current_index]
    
    return array[:unique_index + 1]

print(remove_duplicates_elements([2, 2, 2, 2, 2]))  #output[2]       
print(remove_duplicates_elements([1, 2, 2, 3, 4, 4, 4, 5, 5]))  #output[1,2,3,4,5]
