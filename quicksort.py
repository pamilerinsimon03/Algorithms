# Import necessary libraries
import random
import time
import matplotlib.pyplot as plt
import pandas as pd


# Define a function to sort an array using the quicksort algorithm
def quicksort(arr):
    # If the array has one or zero elements, return it (since it's already sorted)
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot element (in this case, the middle element)
        pivot = arr[len(arr) // 2]
        # Create three lists: left, middle, and right
        left = []
        middle = []
        right = []
        # Iterate over the array
        for i in arr:
            # If the element is less than the pivot, add it to the left list
            if i < pivot:
                left.append(i)
            # If the element is equal to the pivot, add it to the middle list
            elif i == pivot:
                middle.append(i)
            # If the element is greater than the pivot, add it to the right list
            elif i > pivot:
                right.append(i)
        # Recursively sort the left and right lists, and combine them with the middle list
        return quicksort(left) + middle + quicksort(right)


# Define a function to generate a list of random integers
def randomized_list(size):
    # Use a list comprehension to generate a list of random integers
    return [random.randint(0, 1000) for _ in range(size)]


# Define a function to measure the time taken by the quicksort algorithm
def quicksort_time(sizes):
    # Create a list to store the times
    times = []
    # Iterate over the sizes
    for size in sizes:
        # Generate a random list of the given size
        arr = randomized_list(size)
        # Start the timer
        start_time = time.time()
        # Sort the list using quicksort
        quicksort(arr)
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

# Measure the time taken by the quicksort algorithm for each array size
times = quicksort_time(array_sizes)

# Print the results
for i in range(len(array_sizes)):
    sizes = array_sizes[i]
    time_taken = times[i]
    print(f"Array size: {sizes}, Time: {time_taken:.6f} seconds")

# Plot the results using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(
    array_sizes, times, marker="o", linestyle=":", color="b", label="Quicksort Time"
)
plt.title("Quicksort Time Vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Time(seconds)")
plt.grid(True)
plt.legend()
plt.show()

# Create a table using pandas
data = {"Array Size": array_sizes, "Time (seconds)": times}
df = pd.DataFrame(data)
print(df)
