#!/usr/bin/python3
"""
Finds a peak in an unsorted list of integers using binary search.

Args:
- arr (list of int): The unsorted list of integers.

Returns:
- int or None: The peak element if found, None if no peak is found.

Complexity: O(log(n))
"""


def find_peak(arr):
    """
    Finds a peak in an unsorted list of integers using binary search.
    Args:
    - arr (list of int): The unsorted list of integers.

    Returns:
    - int or None: The peak element if found, None if no peak is found.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # Check if mid is a peak
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and \
                (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):

            return arr[mid]
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1  # Search left
        else:
            low = mid + 1  # Search right
    return None  # Peak not found
