import random
import time
import matplotlib.pyplot as plt


def bubble_sort(arr):
    # Sorts an array using the bubble sort algorithm.
    # Args:
    #    arr (list): The array to be sorted.
    # Returns:
    #   None
    # Example:
    #    >>> arr = [5, 2, 8, 3, 1, 6, 4]
    #    >>> bubble_sort(arr)
    #    >>> arr
    #    [1, 2, 3, 4, 5, 6, 8]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def generate_random_array(size):
    # Generates a random array of a given size.
    # Args:
    #    size (int): The size of the array.

    # Returns:
    #    list: A random array of the given size.
    return [random.randint(0, 1000) for _ in range(size)]


def measure_bubble_sort_time(sizes):
    # Measures the time taken to sort arrays of different sizes using bubble sort.

    # Args:
    #    sizes (list): A list of array sizes.

    # Returns:
    #    list: A list of times taken to sort arrays of each size.

    # Example:
    #    >>> sizes = [100, 200, 300, 400, 500]
    #    >>> times = measure_bubble_sort_time(sizes)
    #    >>> times
    #    [0.001234, 0.002567, 0.004321, 0.006789, 0.009012]
    times = []
    for size in sizes:
        arr = generate_random_array(size)
        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
    return times


num_of_sizes = int(input("Enter the number of array sizes: "))
array_sizes = []

for i in range(1, num_of_sizes + 1):
    array_sizes.append(int(input(f"Enter the size of array {i}: ")))


bubble_sort_times = measure_bubble_sort_time(array_sizes)

for i in range(len(array_sizes)):
    size = array_sizes[i]
    time_taken = bubble_sort_times[i]
    print(f"Array size: {size}, Time taken: {time_taken:.6f} seconds")

# Create the plot
plt.figure(figsize=(10, 6))
# This line creates a new figure for plotting. The figsize parameter sets the size of the figure to be 10 inches wide and 6 inches tall. This provides a canvas where we will draw our plot.
plt.plot(
    array_sizes,
    bubble_sort_times,
    marker="o",
    linestyle="-",
    color="b",
    label="Bubble Sort Time",
)
# This line plots the data.
# array_sizes: This is the list of array sizes (x-axis values).
# bubble_sort_times: This is the list of running times (y-axis values).
# marker='o': This specifies that each data point should be marked with a circle ('o').
# linestyle='-': This specifies that the points should be connected with a solid line ('-').
# color='b': This sets the color of the line and markers to blue ('b').
# label='Bubble Sort Time': This sets the label for this plot, which will be used in the legend.

# Add title and labels
plt.title("Bubble Sort Running Time vs. Array Size")
# This sets the title of the plot to "Bubble Sort Running Time vs. Array Size". The title is displayed at the top of the plot.

plt.xlabel("Array Size")
# This sets the label for the x-axis to "Array Size". This label describes what the values on the x-axis represent.

plt.ylabel("Time (seconds)")
# This sets the label for the y-axis to "Time (seconds)". This label describes what the values on the y-axis represent.

# Add a grid for better readability
plt.grid(True)
# This adds a grid to the plot. The grid makes it easier to read the values by providing horizontal and vertical lines across the plot.

# Add a legend
plt.legend()
# This displays the legend on the plot. The legend shows the label defined in the plt.plot function ('Bubble Sort Time'). This helps to identify different lines if you have multiple plots on the same figure.

plt.show()
# This displays the plot on the screen.
