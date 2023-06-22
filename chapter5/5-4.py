def bs_largest(array, low, high):
    mid = (low+high)//2
    if high >= low:
        # base cases
        # mid is largest
        if array[mid] > array[mid-1] and array[mid] > array[mid+1]:
            return array[mid]
        # largest element on right side
        elif array[mid] > array[mid-1]:
            return bs_largest(array, mid+1, high)
        # largest element on left side
        else:
            return bs_largest(array, low, mid-1)


arr = [1, 9, 3, 0]

print(bs_largest(arr, 0, len(arr)-1))
