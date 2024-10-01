import random
from time import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)

# Non-Random Pivot Quicksort
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[i], arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Helper function to call quicksort and average the result over multiple trials
def benchmark_case(arr, num_trials=5):
    total_time = 0
    for _ in range(num_trials):
        arr_copy = arr[:]
        start = time()
        quicksort(arr_copy, 0, len(arr_copy) - 1)
        end = time()
        total_time += (end - start)
    return total_time / num_trials  # Return the average time

# Benchmarking
sizes = [i for i in range(1000, 10001, 2000)]

# Initialize timing lists
totalTimeBest = []
totalTimeWorst = []
totalTimeAvg = []

for size in sizes:
    # Best case: already sorted array
    arrBest = list(range(size))

    # Worst case: reverse sorted array
    arrWorst = arrBest[::-1]

    # Average case: random array with a larger range of numbers
    arrAvg = [random.randint(0, size * 10) for _ in range(size)]

    # Benchmarking
    totalTimeAvg.append(benchmark_case(arrAvg))  # Average case
    totalTimeBest.append(benchmark_case(arrBest))  # Best case
    totalTimeWorst.append(benchmark_case(arrWorst))  # Worst case

# Plotting the results
plt.figure(figsize=(15, 9))

# Plot the benchmark results
plt.plot(sizes, totalTimeBest, label='Best Case', marker='o')
plt.plot(sizes, totalTimeWorst, label='Worst Case', marker='x')
plt.plot(sizes, totalTimeAvg, label='Average Case', marker='s')

plt.legend()
plt.title('Runtime of QuickSort which is non random')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
