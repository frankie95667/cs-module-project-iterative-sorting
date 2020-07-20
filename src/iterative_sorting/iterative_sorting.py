# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # loop through array starting with the index after cur_index and ending 1 before the last index 
        for j in range(cur_index + 1, len(arr)):

            # check if arr[smallest_index] is larger than arr[j]
            if arr[smallest_index] > arr[j]:
                # set smallest_index to j (new smallest value)
                smallest_index = j
        # perform the swap after iterating through list
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # save last index of arr to end_of_arr
    end_of_arr = len(arr) -1
    # set has_swapped to True to enter while loop
    has_swapped = True
    while has_swapped:
        # set has_swapped to false before looping through arr
        # as long as at least 1 swap is performed, continue looping
        has_swapped = False
        for i in range(0, end_of_arr):
            # perform swap when value of i is larger is value of i + 1 
            if arr[i] > arr[i + 1]:
                has_swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        # decprement end of array
        end_of_arr -= 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Get maximum value if not provided
    if maximum is None:
        maximum = 0
        for i in arr:
            # return Error if a negative number is found
            if i < 0:
                return "Error, negative numbers not allowed in Count Sort"

            if i > maximum:
                maximum = i
    # assign an array of maximum size with default values being 0
    counter = [0] * (maximum + 1) 
    for i in arr:
        counter[i] += 1
    # setup a counter for the index of arr
    j = 0
    # loop through counter list
    for i in range(0, len(counter)):
        # while counter[i] is larger than 0, add value to arr in order, then decrement counter[i] and increment j
        while counter[i] > 0:
            arr[j] = i
            j += 1
            counter[i] -= 1
    return arr
