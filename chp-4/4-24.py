# T(O) = O(n)
def sort_neg_pos(array):
    i = -1
    for j in range(len(array)):
        if array[j] < 0:
            i += 1
            array[i], array[j] = array[j], array[i]
    return array


array = [-1, 4, 6, -5, 2, -4, 9]
print(sort_neg_pos(array))
