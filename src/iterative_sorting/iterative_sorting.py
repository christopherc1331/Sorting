# TO-DO: Complete the selection_sort() function below 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
# start at current index, loop through rest of the array to the right, 
# if a smaller value is found, store that index location as smallest.
# create temp variable for current_index value
# swap the smallest index with current index in the array
# current index moves to the right and continues loop


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for k in range(i + 1, len(arr)):
    
            if arr[k] < arr[smallest_index]:
                smallest_index = k

        # temp = arr[cur_index]
        # arr[cur_index] = arr[smallest_index]
        # arr[smallest_index] = temp
        arr[smallest_index], arr[cur_index]  = arr[cur_index], arr[smallest_index]

        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):


    swapped = True
    while swapped == True:
        swapped = False

        for i in range(0, len(arr) -  1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1]  = arr[i + 1], arr[i]
                swapped = True



# Swap Count to track swaps during for loop, if no swaps occur, array is ordered
# When at the end of the list, if swap count is 0, you are done. Else reset swap count to 0 and start over
# Start with first index, compare with next index in list, if greater than next index, switch the two indexes
# Change swap count to 1
# Move to next index and restart the loop

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr