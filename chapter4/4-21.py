def partition(array, low, high):
    pivot = array[high]  # arbitrary choice of pivot
    i = low - 1  # partition i
    for j in range(low, high):
        # move elements smaller than pivot to left of pivot
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    # swap pivot with greater element
    # pivot element falls into correct position
    array[high], array[i+1] = array[i+1], array[high]
    return i + 1


def find_k_largest(array, low, high, k):
    if low < high:
        # get pivot such that left < pivot < right
        pivot = partition(array, low, high)
        # if k-1 elements on the right, then pivot is k largest element
        if (high - pivot) == k - 1:
            return array[pivot]
        # recurse among larger elements
        elif (high - pivot) >= k:
            return find_k_largest(array, pivot + 1, high, k)
        # adjust k for removed larger elements
        else:
            k -= (high-pivot)
            return find_k_largest(array, low, pivot - 1, k)


arr = [8, 7, 2, 1, 0, 9, 6]
size = len(arr)
print(find_k_largest(arr, 0, size - 1, size//2 + 1))
