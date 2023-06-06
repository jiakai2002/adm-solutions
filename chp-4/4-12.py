# (a)


import heapq


def binarySearch(array, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif x < array[mid]:
            return binarySearch(array, x, low, mid - 1)

        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return False


def get_union_a(set1, set2):
    sorted_set1 = []
    heapq.heapify(set1)
    while set1:
        sorted_set1.append(heapq.heappop(set1))
    union = sorted_set1
    for i in set2:
        if binarySearch(sorted_set1, i, 0, len(sorted_set1) - 1) is False:
            union.append(i)
    return union


# (b)


def get_union_b(set1, set2):
    union = set1
    for i in set2:
        if binarySearch(set1, i, 0, len(set1) - 1) is False:
            union.append(i)
    return union
