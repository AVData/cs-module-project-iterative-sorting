# [1, 2, 3, 4, 5, 6, 7, 9, 10]


# assume arr is sorted
def binary_search(arr, target):
    # let's figure out the total size of the array
    lef = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + ritght) // 2

        # check to see if the midpoint elemnt is the target
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            # toss out the left side of the arr
            left = mid + 1

        # otherwise, arr[mid] > target
        else:
            # toss out the right side of the arr
            right = mid - 1

    return - 1
