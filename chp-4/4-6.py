import heapq


def binarySearch(array, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binarySearch(array, x, low, mid - 1)

        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return False


def find_sum_pair_1(s1, s2, x):
    sorted_s1 = []
    heapq.heapify(s1)
    while s1:
        sorted_s1.append(heapq.heappop(s1))
    for i in s2:
        if binarySearch(sorted_s1, x - i, 0, len(sorted_s1) - 1):
            return True


def find_sum_pair_2(s1, s2, x):
    for i in s1:
        for j in s2:
            if x == i + j:
                return True


print(find_sum_pair_1([3, 12, 5, 7, 4, 1], [2, 4, 7, 1, 0, 12, 5], 8))
