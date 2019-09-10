# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        #smallest_index will become the index which holds the next smallest value.
        while cur_index < len(arr):
            if  arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
                cur_index += 1
                if cur_index == len(arr):
                    [arr[i], arr[smallest_index]] = [arr[smallest_index], arr[i]]
            else: 
                cur_index += 1
                if cur_index == len(arr):
                    [arr[i], arr[smallest_index]] = [arr[smallest_index], arr[i]]

                
        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 2):
        i = 0
        num = i
        swaps = 0
        while num < len(arr) - 1:
            if arr[num] > arr[num + 1]:
                [arr[num], arr[num + 1]] = [arr[num + 1], arr[num]]
                num += 1
                swaps += 1
            else:
                num += 1
                if num == len(arr) - 1 and swaps == 0:
                    return arr

    return arr

bubble_sort([2,4,1,9,7,3,5,8,8])

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    
    return arr