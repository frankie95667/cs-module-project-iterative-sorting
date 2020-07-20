def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1
    midpoint = (high - low) // 2
    while high - low > 0:
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] > target:
            high = midpoint 
            midpoint = low + ((high - low) // 2)
        else:
            low = midpoint
            midpoint = low + ((high - low) // 2)


    return -1  # not found
