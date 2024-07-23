# Import necessary libraries
import random
import time
import matplotlib.pyplot as plt
import pandas as pd


# Define a function to sort an array using the merge sort algorithm
def merge_sort(arr):
    # If the array has one or zero elements, return it (since it's already sorted)
    if len(arr) <= 1:
        return arr
    # Find the middle of the array
    mid = len(arr) // 2
    # Recursively sort the left and right halves of the array
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # Merge the sorted halves
    return merge(left_half, right_half)


# Define a function to merge two sorted arrays
def merge(left, right):
    # Create a result array
    result = []
    # Initialize indices for the left and right arrays
    i = j = 0
    # Merge the arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add any remaining elements from the left and right arrays
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Define a function to generate a random list of integers
def random_gen(size):
    # Use a list comprehension to generate a list of random integers
    return [random.randint(0, 10000) for _ in range(size)]


# Define a function to measure the time taken by the merge sort algorithm
def merge_sort_times(sizes):
    # Create a list to store the times
    times = []
    # Iterate over the sizes
    for size in sizes:
        # Generate a random list of the given size
        arr = random_gen(size)
        # Start the timer
        start_time = time.time()
        # Sort the list using merge sort
        merge_sort(arr)
        # Stop the timer
        end_time = time.time()
        # Calculate the time taken and add it to the list
        times.append(end_time - start_time)
    # Return the list of times
    return times


# Ask the user for the number of array sizes
num_of_sizes = int(input("Enter the number of array sizes: "))
# Create a list to store the array sizes
array_sizes = []

# Ask the user for the sizes of the arrays
for i in range(1, num_of_sizes + 1):
    array_sizes.append(int(input(f"Enter the size of array {i}: ")))

# Measure the time taken by the merge sort algorithm for each array size
times = merge_sort_times(array_sizes)

# Plot the results using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(
    array_sizes, times, marker="o", linestyle="-", color="b", label="Merge Sort Time"
)
plt.title("Merge Sort Times Vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()
plt.show()

# Plot the results using a bar chart
plt.figure(figsize=(10, 6))
plt.bar(array_sizes, times, color="b", width=20000)
plt.title("Merge Sort Times Vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()

# Create a table using pandas
data = {"Array Size": array_sizes, "Times": times}
df = pd.DataFrame(data)
print(df)
