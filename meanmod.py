import statistics

def calculate_statistics(numbers):
    """Calculate and return the mean, median, and mode of a list of numbers."""
    
    # Calculate mean
    mean_value = statistics.mean(numbers)
    
    # Calculate median
    median_value = statistics.median(numbers)
    
    # Calculate mode
    try:
        mode_value = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode_value = "No unique mode"

    return mean_value, median_value, mode_value

# Example usage
numbers = [1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9]

mean, median, mode = calculate_statistics(numbers)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
