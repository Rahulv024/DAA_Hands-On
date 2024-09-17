def merge_arrays(array1, array2):
    print(f"Merging {array1} and {array2}")
    merged_array = []
    i, j = 0, 0  

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1

    while i < len(array1):
        merged_array.append(array1[i])
        i += 1

    while j < len(array2):
        merged_array.append(array2[j])
        j += 1

    print(f"The Result of merging: {merged_array}\n")
    return merged_array

def merge_karrays(arrays):
    if not arrays:
        return []
    
    print(f"Starting with arrays: {arrays}\n")

    while len(arrays) > 1:
        merged_arrays = []
        
        for i in range(0, len(arrays), 2):
            if i + 1 < len(arrays):
                merged_arrays.append(merge_arrays(arrays[i], arrays[i + 1]))
            else:
                merged_arrays.append(arrays[i])
        
        arrays = merged_arrays 
        print(f"After merging we have: {arrays}\n")

    print(f"The final merged array: {arrays[0]}")
    return arrays[0]

arrays_1 = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
arrays_2 = [[1, 3, 7], [2, 4, 8], [9, 10, 11]]

print("Example 1:")
merge_karrays(arrays_1) 

print("\nExample 2:")
merge_karrays(arrays_2)
