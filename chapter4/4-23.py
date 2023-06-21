
#  T(O) = O(N)
def partition(array, low, high, colour):
    i = low - 1  # partition i
    for j in range(low, high):
        # e.g. all red elements to left of partition
        if array[j] == colour:  # Examine(array, j)
            i += 1
            array[i], array[j] = array[j], array[i]  # Swap(array, i, j)
    return i + 1


def sort_colours(array, low, high):
    # move all red to left
    new_low = partition(array, low, high, 'red')
    # move all white to left
    partition(array, new_low, high, 'white')
    return array


array = ['white', 'blue', 'blue', 'red',
         'white', 'red', 'blue', 'white', 'red']
size = len(array)
print(sort_colours(array, 0, size))
