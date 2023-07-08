def binary_search(array, low, high):
    mid = (low+high)//2
    i = mid+1
    if high >= low:
        # base case
        if array[mid] == i:
            return array[mid]
        # search element in left side
        elif array[mid] > i:
            return binary_search(array, low, mid-1)
        # search element in right side
        else:
            return binary_search(array, mid+1, high)
    else:
        return False


arr = [2, 3, 4, 5, 6, 7]

print(binary_search(arr, 0, len(arr)-1))
