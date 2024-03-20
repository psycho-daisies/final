"""
Midterm Library: Quick Sort
Troy Brunette
CS240
I found the CS Dojo YouTube video on Quicksort a great resource to help with this assignment."""

"""Uses Binary Search from past assignment and a couple functions for reading the provided numbers text file"""

def quicksort(arr, l, r):
    if l >= r:  # BASE CASE
        return
    # Recursive CASE: partition / choosing a pivot
    p = partition(arr, l, r)

    # calling quicksort on the two groups
    quicksort(arr, l, p - 1)
    quicksort(arr, p + 1, r)

    return arr


# Separates numbers into two groups
# Numbers less than the pivot
# Numbers greater than the pivot
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])

    return i + 1


# Testing Quicksort on a small array
# numbers = [2, 9, 6, 3, 7, 5, 8, 4, 1]
# print(quicksort(numbers, 0, len(numbers) - 1))
