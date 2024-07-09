# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    while len(arrA) > 0 or len(arrB) > 0:
        # print(arrA)
        # print(arrB)
        # print(merged_arr)
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] > arrB[0]:
                merged_arr.append(arrB[0])
                arrB.remove(arrB[0])
            else:
                merged_arr.append(arrA[0])
                arrA.remove(arrA[0])
        elif len(arrA) > 0:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        elif len(arrB) > 0:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        leftArray = arr[0:len(arr)//2]
        rightArray = arr[len(arr)//2:]
        left = merge_sort(leftArray)
        right = merge_sort(rightArray)
        arr = merge(left, right)

    return arr


# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr

