def get_largest(array, k):
    return array[k-1]


def get_largest_bs(array, low, high):
    if high >= low:
        mid = (low+high)//2
        # two base cases
        # mid is largest
        if mid < high and array[mid] > array[mid+1]:
            return array[mid]
        # mid - 1 is largest
        elif mid < high and array[mid-1] > array[mid]:
            return array[mid-1]
        # check whether to search left or right half
        elif array[high] > array[mid]:
            return get_largest_bs(array, low, mid-1)
        else:
            return get_largest_bs(array, mid+1, high)


arr = [27, 5, 15, 23, 24, 25]

print(get_largest_bs(arr, 0, len(arr)-1))
