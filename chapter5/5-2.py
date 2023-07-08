def bs_missing(array, low, high):
    mid = (low+high)//2
    if high >= low:
        # two base cases
        # missing integer left of mid
        if array[mid]-array[mid-1] > 1:
            return array[mid]-1
        # missing integer right of mid
        elif array[mid+1]-array[mid] > 1:
            return array[mid]+1
        # search left or right side
        else:
            # missing integer in right side
            length = array[high]-array[mid]+1
            if length > len(array[mid:high+1]):
                return bs_missing(array, mid+1, high)
            # missing integer in left side
            else:
                return bs_missing(array, low, mid-1)


arr = [1, 2, 4, 5, 6, 7]

print(bs_missing(arr, 0, len(arr)-1))
