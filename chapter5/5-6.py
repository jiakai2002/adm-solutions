# job is to find smallest non-successive element in a
# we will use a left-biased binary search approach
def binary_search(array, low, high):
    if array[0] > 1:
        return 1
    mid = (high+low)//2
    min = None
    if high > low:
        # two base cases with at least 2 elements
        # 1) mid-1 and mid not successive
        if array[mid]-array[mid-1] > 1:
            min = array[mid-1]+1
            # continue to search left if left side has unsuccessive element
            length = array[mid-1]-array[low]+1
            if length > len(array[low:mid+1]):
                return binary_search(array, low, mid-1)
            else:
                return min
        # 2) mid and mid+1 not successive
        elif array[mid+1]-array[mid] > 1:
            min = array[mid]+1
            # continue to search left if left side has unsuccessive element
            length = array[mid-1]-array[low]+1
            if length > len(array[low:mid+1]):
                return binary_search(array, low, mid-1)
            else:
                return min
        else:
            # search left side
            length = array[mid]-array[low]+1
            if length > len(array[low:mid+1]):
                return binary_search(array, low, mid-1)
            # search right side if min not found
            elif not min:
                return binary_search(array, mid+1, high)
    return arr[-1]


arr = [1, 2, 3, 5]

print(binary_search(arr, 0, len(arr)-1))
