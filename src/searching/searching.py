def linear_search(arr, target): 
    # iterate through arr
    for i in range(0, len(arr)):
        # return index when target matches arr[i]
        if arr[i] == target:
            return i # found

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # initialize the low value to 0
    low = 0
    # initialize midpoint (high - low) // 2
    high = len(arr) - 1
    # initialize midpoint (high - low) // 2
    midpoint = (high - low) // 2
    # loop while high - low > 0
    while high - low > 0:
        
        # if arr[midpoint] equals target
        if arr[midpoint] == target:
            # return midpoint
            return midpoint
        
        # else if midpoint value is higher than target
        elif arr[midpoint] > target:
            # set high to midpoint
            high = midpoint 
            # set midpoint to low + ((high - low) // 2)
            midpoint = low + ((high - low) // 2)

        # else target is found in upper half.
        else:
            # set low to midpoint
            low = midpoint
            # set midpoint to low + ((high - low) // 2)
            midpoint = low + ((high - low) // 2)


    return -1  # not found
