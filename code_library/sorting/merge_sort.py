"""
Midterm Library: Merge Sort
Troy Brunette
CS240
"""

"""Uses Binary Search from past assignment and a couple functions for reading the provided numbers text file"""


# Merge Sort recursively divides the array into sub-arrays and merges it back in sorted order
def merge_sort(arr):
    if len(arr) <= 1:  # BASE CASE
        return arr

    # Divide & Conquer: split the array into two sub-arrays: left & right
    mid = len(arr) // 2
    left = arr[:mid]  # from start of array to the middle
    right = arr[mid:]  # from the middle to the end

    # RECURSIVE CASE: recursively splits each sub-array in half
    merge_sort(left)
    merge_sort(right)

    # Sorts and then merges the sub-arrays
    return merge(arr, left, right)

# Merge compares the elements in the sub-arrays and puts them back together in order
def merge(arr, left, right):
    i = j = k = 0

    # Compares the sub-arrays and puts them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Merges the sub-arrays
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    # Copy the remaining elements
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

a = [3, 5, 1, 8, 6, 4, 2, 7]
b = a.copy()
print("Unsorted: ", b)
print("Sorted:   ", merge_sort(a))

