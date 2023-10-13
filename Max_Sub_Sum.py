def max_subarray_sum(arr):
    n = len(arr)
    
    # Initialize variables to keep track of the maximum sum and current sum
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, n):
        # Choose between extending the current subarray or starting a new one
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print("Maximum Subarray Sum:", result)
