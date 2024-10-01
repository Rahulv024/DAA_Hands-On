```
import random

# Quicksort with a fixed pivot selection
def quicksort_non_random(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_non_random(arr, low, pivot_index - 1)
        quicksort_non_random(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    return i + 1

# Quicksort with a random pivot selection
def quicksort_random(arr, low, high):
    if low < high:
        pivot_index = partition_random(arr, low, high)
        quicksort_random(arr, low, pivot_index - 1)
        quicksort_random(arr, pivot_index + 1, high)

def partition_random(arr, low, high):
    random_pivot_index = random.randint(low, high)  # Select a random pivot
    arr[high], arr[random_pivot_index] = arr[random_pivot_index], arr[high]  # Swap the random pivot with the last element
    return partition(arr, low, high)  # Use the standard partitioning method

# Execution block for testing
if __name__ == "__main__":
    # Sample array for testing
    test_array1 = [24, 18, 45, 10, 7, 1, 99]
    test_array2 = test_array1.copy()  # Duplicate the array for random pivot quicksort
    
    # Display the original array
    print("The original array is:", test_array1)

    # Sort using the fixed pivot quicksort
    quicksort_non_random(test_array1, 0, len(test_array1) - 1)
    print("Sorted array with fixed pivot:", test_array1)

    # Sort using the random pivot quicksort
    quicksort_random(test_array2, 0, len(test_array2) - 1)
    print("Sorted array with random pivot:", test_array2)
```

