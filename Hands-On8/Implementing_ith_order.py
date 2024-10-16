import random

#partition for quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

# Quicksort function to find ith order
def quickselect(arr, low, high, i):
    if low == high:
        return arr[low]

    # Partition the array
    pivot_index = partition(arr, low, high)

    # pivot is in its final sorted position
    if i == pivot_index:
        return arr[i]
    elif i < pivot_index:
        return quickselect(arr, low, pivot_index - 1, i)
    else:
        return quickselect(arr, pivot_index + 1, high, i)

# Function to find ith smallest element
def ith_order_statistic(arr, i):
    if i < 0 or i >= len(arr):
        raise IndexError("Index out of bounds")
    return quickselect(arr, 0, len(arr) - 1, i)

# Example
arr = [7,18,69,37,45,1,29]
i = 3  # Find the 4th smallest element as index starts from 0
result = ith_order_statistic(arr, i)
print(f"The {i+1}th smallest element is: {result}")


#OUTPUT: 
#The 4th smallest element is: 23
