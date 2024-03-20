"""
Midterm Library: Selection Sort
Troy Brunette
CS240
"""
def selection_sort(arr):
    # loop through all elements
    for i in range(len(arr) - 1):
        # set minimum
        min_index = i
        for j in range(i + 1, len(arr)):
            # if arr[min_index] > arr[j]:  # SORTS THEM AS STRINGS
            if int(arr[j]) < int(arr[min_index]):  # SORTS THEM AS INT
                min_index = j
        # swap
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    return arr



# a = [3, 5, 1, 8, 6, 4, 2, 7]
# b = a.copy()
# print("Unsorted: ", b)
# print("Sorted:   ", selection_sort(a))
