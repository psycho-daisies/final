"""
Midterm Library: Insertion Sort
Troy Brunette
CS240
"""
def insertion_sort(arr):
    # loop through elements starting from index 1
    for i in range(1, len(arr)):
        temp = arr[i]  # element to put in sorted order
        j = i - 1  # sets j to the index before index i
        # check if temp is less than the elements to the left and insert it into the sorted position
        while j >= 0 and int(temp) < int(arr[j]):
            arr[j + 1] = arr[j]  # moves elements over to the right
            j -= 1  # moves j index towards 0

        arr[j + 1] = temp  # places element into sorted position
    return arr

# Testing insertion sort
# a = [3, 5, 1, 8, 6, 4, 2, 7]
# b = a.copy()
# print("Unsorted: ", b)
# print("Sorted:   ", insertion_sort(a))
