"""
Midterm Library: Linear Search
Troy Brunette
CS240
"""

def linear_search_recursive(array, target_number, index):
    # Base case: target not found at any index
    if index >= len(array):
        return -1

        # Checks for number, return index when found
    if array[index] == target_number:
        return index

        # Recursively call function to keep searching
    index += 1
    return linear_search_recursive(array, target_number, index)


# Helper function
def linear_search(array, target_number):
    return linear_search_recursive(array, target_number, 0)