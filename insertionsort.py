# Import necessary libraries
import random  # for generating random numbers
import time  # for measuring time
import matplotlib.pyplot as plt  # for plotting graphs
import pandas as pd  # for data manipulation and analysis


# Function to generate a list of random numbers
def random_generator(size):
    # Return a list of 'size' random integers between 0 and 1000
    return [random.randint(0, 1000) for _ in range(size)]


# Function to perform insertion sort on a list
def insertion_sort(arr):
    # Iterate over the list starting from the second element
    for j in range(1, len(arr)):
        # Store the current element as the key
        key = arr[j]
        # Initialize a variable to keep track of the previous element
        i = j - 1
        # Shift elements greater than the key to the right
        while i > -1 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        # Insert the key at the correct position
        arr[i + 1] = key
    # Return the sorted list
    return arr


# Function to measure the time taken by insertion sort for different array sizes
def insert_sort_times(sizes):
    # Initialize a list to store the times
    times = []
    # Iterate over the array sizes
    for size in sizes:
        # Generate a random array of the given size
        arr = random_generator(size)
        # Record the start time
        start_time = time.time()
        # Perform insertion sort
        insertion_sort(arr)
        # Record the end time
        end_time = time.time()
        # Calculate the time taken and append it to the list
        times.append(end_time - start_time)
    # Return the list of times
    return times


# Ask the user for the number of array sizes to test
num_of_sizes = int(input("Enter the number of array sizes: "))
# Initialize a list to store the array sizes
array_size = []

# Ask the user for each array size
for i in range(1, num_of_sizes + 1):
    array_size.append(int(input(f"Enter the size of array {i}: ")))

# Measure the time taken by insertion sort for each array size
times = insert_sort_times(array_size)

# Plot a line graph of time vs array size
plt.figure(figsize=(10, 6))
plt.plot(
    array_size, times, marker="o", linestyle="-", color="b", label="Insert Sort Time"
)
plt.title("Insert Sort Time Vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()
plt.show()

# Plot a bar graph of time vs array size
plt.figure(figsize=(10, 6))
plt.bar(array_size, times, color="r", width=150)
plt.title("Insert Sort Time Vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()

# Create a pandas DataFrame to store the data
data = {"Array Size": array_size, "Time (seconds)": times}
df = pd.DataFrame(data)
# Print the DataFrame
print(df)
